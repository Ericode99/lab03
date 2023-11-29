import sys
from architecture import OPS, OP_MASK, OP_SHIFT

def disassemble_line(line):
    instruction = int(line, 16)
    op_code = instruction & OP_MASK
    reg1 = (instruction >> OP_SHIFT) & OP_MASK
    reg2_or_val = (instruction >> (2 * OP_SHIFT)) & OP_MASK

    for name, details in OPS.items():
        if details["code"] == op_code:
            if details["fmt"] == "--":
                return name
            elif details["fmt"] == "rv":
                return f"{name} R{reg1} {reg2_or_val}"
            elif details["fmt"] == "rr":
                return f"{name} R{reg1} R{reg2_or_val}"
            elif details["fmt"] == "r-":
                return f"{name} R{reg1}"
    return "unknown"

def disassemble_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(disassemble_line(line.strip()) + "\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 disassembler.py input_file.mx output_file.as")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]
    disassemble_file(input_file, output_file)

if __name__ == "__main__":
    main()
