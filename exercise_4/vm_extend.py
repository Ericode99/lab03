import sys

from architecture import VMState
from vm_step import VirtualMachineStep
from architecture import RAM_LEN


class VirtualMachineExtend(VirtualMachineStep):
    # [init]
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(reader, writer)
        self.handlers = {
            "d": self._do_disassemble,
            "dis": self._do_disassemble,
            "i": self._do_ip,
            "ip": self._do_ip,
            "m": self._do_memory,
            "memory": self._do_memory,
            "q": self._do_quit,
            "quit": self._do_quit,
            "r": self._do_run,
            "run": self._do_run,
            "s": self._do_step,
            "step": self._do_step,
        }

    # [/init]

    def get_index_of_breakpoint(self, command):
        assert len(command) == 2, f"format must be 'command' 'index'"
        index = None
        try:
            index = int(command[1])
            assert index < RAM_LEN, f"please provide an index within the bounds of RAM"
        except ValueError:
            print("Please provide a valid index (int) for the breakpoint")
        return index





    # [interact]
    def interact(self, addr):
        prompt = "".join(sorted({key[0] for key in self.handlers}))
        interacting = True
        while interacting:
            try:
                command = self.read(f"{addr:06x} [{prompt}]> ")
                if not command:
                    continue
                # add ability of user entering range of memory display, breakpoint setting/clearing at certain index
                elif isinstance(command, list) and "memory".startswith(command[0]):
                    start, stop = self.get_memory_range(command)
                    self.show(start=start, stop=stop)
                elif isinstance(command, list) and "break".startswith(command[0]):
                    index = self.get_index_of_breakpoint(command)
                    interacting = self.handlers[command[0]](index)
                elif isinstance(command, list) and "clear".startswith(command[0]):
                    index = self.get_index_of_breakpoint(command)
                    interacting = self.handlers[command[0]](index)
                else:
                    # get all the functions which are relevant for interacting(debugger) -> start with _do_
                    OPERATIONS = {
                        func_name.replace("_do_", ""): getattr(self, func_name)
                        for func_name in dir(self) if func_name.startswith("_do_") and callable(getattr(self, func_name))
                    }
                    # call associate function with the prefix of 'command'
                    method = None
                    for name in OPERATIONS:
                        if name.startswith(command):
                            method = OPERATIONS[name]
                    if not method:
                        self.write(f"Unknown command {command}")
                    else:
                        interacting = method(self.ip)
            except EOFError:
                self.state = VMState.FINISHED
                interacting = False

    # [/interact]

    def _do_disassemble(self, addr):
        self.write(self.disassemble(addr, self.ram[addr]))
        return True

    def _do_ip(self, addr):
        self.write(f"{self.ip:06x}")
        return True

    # [memory]
    def _do_memory(self, addr):
        self.show()
        return True

    # [/memory]

    def _do_quit(self, addr):
        self.state = VMState.FINISHED
        return False

    def _do_run(self, addr):
        self.state = VMState.RUNNING
        return False

    # [step]
    def _do_step(self, addr):
        self.state = VMState.STEPPING
        return False
    # [/step]


if __name__ == "__main__":
    VirtualMachineExtend.main()
