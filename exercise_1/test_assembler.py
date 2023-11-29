import pytest
import subprocess

# Define a fixture to run the assembler and generate .mx files
@pytest.fixture(scope="module", autouse=True)
def setup_assembler():
    # Define the commands to be executed
    commands = [
        ['python3', '../vm/assembler.py', 'assemblyPrograms/basicOp.as', 'vmInstructions/basicOp.mx'],
        ['python3', '../vm/assembler.py', 'assemblyPrograms/copyPrntMem.as', 'vmInstructions/copyPrntMem.mx'],
        ['python3', '../vm/assembler.py', 'assemblyPrograms/memOpBeq.as', 'vmInstructions/memOpBeq.mx'],
        ['python3', '../vm/assembler.py', 'assemblyPrograms/memOpBne.as', 'vmInstructions/memOpBne.mx']
    ]

    # Run the commands
    for command in commands:
        subprocess.run(command)

# Test functions
def test_assembler_basic_operation_program():
    with open("vmInstructions/basicOp.mx", "r") as file:
        generated_output = file.readlines()
    expected_output = ["050002\n", "030102\n", "010006\n", "010007\n", "00000a\n", "000001\n"]
    assert generated_output == expected_output

def test_assembler_copy_print_memory_program():
    with open("vmInstructions/copyPrntMem.mx", "r") as file:
        generated_output = file.readlines()
    expected_output = ["1e0002\n", "630102\n", "000105\n", "000204\n", "00020b\n", "000001\n"]
    assert generated_output == expected_output

def test_assembler_memory_operations_branch_equal_program():
    with open("vmInstructions/memOpBeq.mx", "r") as file:
        generated_output = file.readlines()
    expected_output = ["0a0002\n", "000102\n", "000105\n", "000203\n", "070208\n", "010302\n", "00030a\n", "020302\n", "00030a\n", "000001\n"]
    assert generated_output == expected_output

def test_assembler_memory_operations_branch_notEqual_program():
    with open("vmInstructions/memOpBne.mx", "r") as file:
        generated_output = file.readlines()
    expected_output = ["0a0002\n", "140102\n", "000105\n", "000203\n", "070209\n", "010202\n", "00020a\n", "00020a\n", "000001\n"]
    assert generated_output == expected_output
