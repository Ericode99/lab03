from architecture import NUM_REG, OP_MASK, OP_SHIFT, OPS, RAM_LEN
import sys

OPS_LOOKUP = {value["code"]: key for key, value in OPS.items()}

class Disassambler:
    def decode(self, instruction):
        op = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg0 = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg1 = instruction & OP_MASK
        return op, arg0, arg1

    def disassemble(self, line):
        instruction = int(line.strip(), 16) 
        op, arg0, arg1 = self.decode(instruction)
        assert op in OPS_LOOKUP, f"Unknown op code {op} at {line}"
        for name, details in OPS.items():
            if details["code"] == op:
                if details["fmt"] == "--":
                    return name
                elif details["fmt"] == "rv":
                    return f"{name} R{arg0} {arg1}"
                elif details["fmt"] == "rr":
                    return f"{name} R{arg0} R{arg1}"
                elif details["fmt"] == "r-":
                    return f"{name} R{arg0}"
        return "unknown"

    def disassemble_file(self, input_file, output_file):
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                outfile.write(self.disassemble(line.strip()) + "\n")

def main(disassambler_cls):
    if len(sys.argv) != 3:
        print("Usage: python3 disassembler.py input_file.mx output_file.as")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]
    disassambler = disassambler_cls()
    disassambler.disassemble_file(input_file, output_file)

if __name__ == "__main__":
    main(Disassambler)