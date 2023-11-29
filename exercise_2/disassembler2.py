from architecture import NUM_REG, OP_MASK, OP_SHIFT, OPS, RAM_LEN, VMState

OPS_LOOKUP = {value["code"]: key for key, value in OPS.items()}
# [/lookup]

def decode(instruction):
        """Decode an instruction to get an op code and its operands."""
        op = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg0 = instruction & OP_MASK
        instruction >>= OP_SHIFT
        arg1 = instruction & OP_MASK
        return op, arg0, arg1

def disassemble(line):
        addr = line
        instruction = ram(addr)
        op, arg0, arg1 = decode(instruction)
        assert op in OPS_LOOKUP, f"Unknown op code {op} at {addr}"
        return f"{OPS_LOOKUP[op]} | {arg0} | {arg1}"

def disassemble_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            outfile.write(disassemble(line.strip()) + "\n")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 disassembler.py input_file.mx output_file.as")
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]
    disassemble_file(input_file, output_file)

if __name__ == "__main__":
    main()