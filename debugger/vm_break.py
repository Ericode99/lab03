import sys

from architecture import OPS, VMState
from vm_extend import VirtualMachineExtend


class VirtualMachineBreak(VirtualMachineExtend):
    # [init]
    def __init__(self):
        super().__init__()
        self.breaks = {}
        self.watchpoints = {}
        self.handlers |= {
            "b": self._do_breakpoint,
            "break": self._do_breakpoint,
            "c": self._do_clear_breakpoint,
            "clear": self._do_clear_breakpoint,
            "w": self._do_watchpoint,
            "watchpoint": self._do_watchpoint
        }

    # [/init]

    # [show]
    def show(self, start=-1, stop=-1):
        super().show(start=start, stop=stop)
        if self.breaks:
            self.write("-" * 6)
            for key, instruction in self.breaks.items():
                # adjust so that if the user wants to see range of memory the breakpoints only gets shown if its
                # original address is within the provided range
                if key >= start:
                    self.write(f"{key:06x}: {self.disassemble(key, instruction)}")

    # [/show]

    # [run]
    def run(self):
        self.state = VMState.STEPPING
        while self.state != VMState.FINISHED:
            instruction = self.ram[self.ip]
            op, arg0, arg1 = self.decode(instruction)

            if not op in [1, 5, 8, 9, 10, 11, 15, 16] and arg0 in self.watchpoints:
                self.ram[arg0] = self.watchpoints[arg0]
                self.state = VMState.FINISHED
            elif op == OPS["brk"]["code"]:
                original = self.breaks[self.ip]
                op, arg0, arg1 = self.decode(original)
                self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)
            else:
                if self.state == VMState.STEPPING:
                    self.interact(self.ip)
                self.ip += 1
                self.execute(op, arg0, arg1)

    # [/run]

    # [add]
    def _do_breakpoint(self, addr):
        if self.ram[addr] == OPS["brk"]["code"]:
            return
        self.breaks[addr] = self.ram[addr]
        self.ram[addr] = OPS["brk"]["code"]
        return True

    # [/add]

    # [clear]
    def _do_clear_breakpoint(self, addr):
        if self.ram[addr] != OPS["brk"]["code"]:
            return
        self.ram[addr] = self.breaks[addr]
        del self.breaks[addr]
        return True

    # [/clear]

    def _do_watchpoint(self, addr):
        self.watchpoints[addr] = self.ram[addr]
        return True


if __name__ == "__main__":
    VirtualMachineBreak.main()
