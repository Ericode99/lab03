import sys

from architecture import OPS, VMState
from vm_base import VirtualMachineBase

# [lookup]
OPS_LOOKUP = {value["code"]: key for key, value in OPS.items()}


# [/lookup]

# [derive]
class VirtualMachineStep(VirtualMachineBase):
    # [/derive]
    # [init]
    def __init__(self, reader=input, writer=sys.stdout):
        super().__init__(writer)
        self.reader = reader

    # [/init]

    # [run]
    def run(self):
        self.state = VMState.STEPPING
        while True:
            if self.state == VMState.STEPPING:
                self.interact(self.ip)
            if self.state == VMState.FINISHED:
                break
            instruction = self.ram[self.ip]
            self.ip += 1
            op, arg0, arg1 = self.decode(instruction)
            self.execute(op, arg0, arg1)

    # [/run]

    # return the memory range the user wants to inspect (entered through input in form of e.g. 'm' 0 1
    def get_memory_range(self, command):
        start = -1
        stop = -1
        try:
            start = int(command[1])
        except ValueError:
            print("please input a valid memory address in form of int")
            return start, stop

        if len(command) < 3:
            return start, stop
        try:
            stop = int(command[2])
        except ValueError:
            print("please input two valid memory addresses in form of ints")
            return -1, -1
        return start, stop

    # [interact]
    def interact(self, addr):
        while self.state == VMState.STEPPING:
            try:
                command = self.read(f"{addr:06x} [dmqrs]> ")
                if not command:
                    continue
                elif isinstance(command, list) and command[0] in {"m", "memory"}:
                    start, stop = self.get_memory_range(command)
                    self.show(start=start, stop=stop)
                elif command in {"d", "dis"}:
                    self.write(self.disassemble(addr, self.ram[addr]))
                elif command in {"m", "memory"}:
                    self.show()
                elif command in {"q", "quit"}:
                    self.state = VMState.FINISHED
                    break
                elif command in {"r", "run"}:
                    self.state = VMState.RUNNING
                    break
                elif command in {"s", "step"}:
                    break
                else:
                    self.write(f"Unknown command '{command}'")
            except EOFError:
                self.state = VMState.FINISHED

    # [/interact]

    # [disassemble]
    def disassemble(self, addr, instruction):
        op, arg0, arg1 = self.decode(instruction)
        assert op in OPS_LOOKUP, f"Unknown op code {op} at {addr}"
        return f"{OPS_LOOKUP[op]} | {arg0} | {arg1}"

    # [/disassemble]

    # [read]
    def read(self, prompt):
        input = self.reader(prompt).strip()
        input = input.split()
        if len(input) > 1:
            return input
        return input[0] if len(input) > 0 else None
    # [/read]


if __name__ == "__main__":
    VirtualMachineStep.main()
