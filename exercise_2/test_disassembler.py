import pytest
import subprocess
from disassembler import Disassambler

@pytest.mark.parametrize("line, expected", [
    ("000001", "hlt"),
    ("000202", "ldc R2 0"),
    ("000303", "ldr R3 R0"),
])

def test_disassemble(line, expected):
    disasambler = Disassambler()
    assert disasambler.disassemble(line) == expected

def test_disassembler_basic_operation_program():
    command = ['python3', 'disassembler.py', 'input_file.mx', 'output_file.as']
    subprocess.run(command)

    with open("output_file.as", "r") as file:
        generated_output = file.readlines()
    expected_output = ["ldc R0 5\n", "ldc R1 3\n", "add R0 R1\n", "sub R0 R1\n", "prr R0\n", "hlt\n"]
    assert generated_output == expected_output