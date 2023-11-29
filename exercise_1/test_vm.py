import pytest
#from vm.assembler import Assembler  # Adjust the import path as needed
import subprocess

# Define the command to be executed





def test_vm_basic_operation_program():
    # Run the VM subprocess and capture its output
    basicOp = ['python3', '../vm/vm.py', 'vmInstructions/basicOp.mx', 'vmOutput/basicOp.out']
    result = subprocess.run(basicOp, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Extract the standard output
    generated_output = result.stdout.strip()

    # Define the expected output
    expected_output = ">> 5"  # Assuming the output is just the number 5 as a string

    # Assert that the generated output matches the expected output
    assert generated_output == expected_output

def test_vm_copy_print_memory_program():
    # Run the VM subprocess and capture its output
    copyPrntMem = ['python3', '../vm/vm.py', 'vmInstructions/copyPrntMem.mx', 'vmOutput/copyPrntMem.out']
    result = subprocess.run(copyPrntMem, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Extract the standard output
    generated_output = result.stdout.strip()

    # Define the expected output
    expected_output = ">> 99"  # Assuming the output is just the number 5 as a string

    # Assert that the generated output matches the expected output
    assert generated_output == expected_output

def test_vm_memory_operations_branch_equal_program():
    memOpBeq = ['python3', '../vm/vm.py', 'vmInstructions/memOpBeq.mx', 'vmOutput/memOpBeq.out']
    # Run the VM subprocess and capture its output
    result = subprocess.run(memOpBeq, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Extract the standard output
    generated_output = result.stdout.strip()

    # Define the expected output
    expected_output = ">> 2"  # Assuming the output is just the number 5 as a string

    # Assert that the generated output matches the expected output
    assert generated_output == expected_output

def test_vm_memory_operations_branch_notEqual_program():
    memOpBne = ['python3', '../vm/vm.py', 'vmInstructions/memOpBne.mx', 'vmOutput/memOpBne.out']
    # Run the VM subprocess and capture its output
    result = subprocess.run(memOpBne, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Extract the standard output
    generated_output = result.stdout.strip()

    # Define the expected output
    expected_output = ">> 20"  # Assuming the output is just the number 5 as a string

    # Assert that the generated output matches the expected output
    assert generated_output == expected_output