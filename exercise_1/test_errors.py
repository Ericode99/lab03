import pytest
#from vm.assembler import Assembler  # Adjust the import path as needed
import subprocess

# Define the command to be executed


def test_error_out_of_memory_program():
    # Run the VM subprocess and capture its standard error output
    outOfMemory = ['python3', '../vm/vm.py', 'errorAssemblyPrograms/out_of_memory.mx', 'errorAssemblyPrograms/out_of_memory.out']
    result = subprocess.run(outOfMemory, stderr=subprocess.PIPE, text=True)

    # Extract the standard error
    generated_error = result.stderr.strip()

    # Check if the expected error message is in the standard error output
    assert "AssertionError: Program too long" in generated_error

def test_error_invalid_instruction_program():
    invalidInstruction = ['python3', '../vm/vm.py', 'errorAssemblyPrograms/invalid_instruction.mx', 'errorAssemblyPrograms/invalid_instruction.out']
    # Run the VM subprocess and capture its standard error output
    result = subprocess.run(invalidInstruction, stderr=subprocess.PIPE, text=True)

    # Extract the standard error
    generated_error = result.stderr.strip()

    # Check if the expected error message is in the standard error output
    assert "AssertionError: Unknown op" in generated_error




    #pytest --cov=vm --cov=assembler --cov=test_assembler --cov=test_vm --cov=test_errors