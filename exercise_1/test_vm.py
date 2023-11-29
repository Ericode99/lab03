import pytest
import subprocess

def test_vm_basic_operation_program():
    basicOp = ['python3', '../vm/vm.py', 'vmInstructions/basicOp.mx', 'vmOutput/basicOp.out']
    result = subprocess.run(basicOp, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    generated_output = result.stdout.strip()
    expected_output = ">> 5"
    assert generated_output == expected_output

def test_vm_copy_print_memory_program():
    copyPrntMem = ['python3', '../vm/vm.py', 'vmInstructions/copyPrntMem.mx', 'vmOutput/copyPrntMem.out']
    result = subprocess.run(copyPrntMem, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    generated_output = result.stdout.strip()
    expected_output = ">> 99" 
    assert generated_output == expected_output

def test_vm_memory_operations_branch_equal_program():
    memOpBeq = ['python3', '../vm/vm.py', 'vmInstructions/memOpBeq.mx', 'vmOutput/memOpBeq.out']
    result = subprocess.run(memOpBeq, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    generated_output = result.stdout.strip()
    expected_output = ">> 2"
    assert generated_output == expected_output

def test_vm_memory_operations_branch_notEqual_program():
    memOpBne = ['python3', '../vm/vm.py', 'vmInstructions/memOpBne.mx', 'vmOutput/memOpBne.out']
    result = subprocess.run(memOpBne, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    generated_output = result.stdout.strip()
    expected_output = ">> 20"
    assert generated_output == expected_output