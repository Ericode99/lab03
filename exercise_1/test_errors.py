import pytest
import subprocess

def test_error_out_of_memory_program():
    outOfMemory = ['python3', '../vm/vm.py', 'errorAssemblyPrograms/out_of_memory.mx', 'errorAssemblyPrograms/out_of_memory.out']
    result = subprocess.run(outOfMemory, stderr=subprocess.PIPE, text=True)

    generated_error = result.stderr.strip()
    assert "AssertionError: Program too long" in generated_error

def test_error_invalid_instruction_program():
    invalidInstruction = ['python3', '../vm/vm.py', 'errorAssemblyPrograms/invalid_instruction.mx', 'errorAssemblyPrograms/invalid_instruction.out']
    result = subprocess.run(invalidInstruction, stderr=subprocess.PIPE, text=True)

    generated_error = result.stderr.strip()
    assert "AssertionError: Unknown op" in generated_error