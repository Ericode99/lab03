import pytest
from vm.assembler import Assembler  # Adjust import path as needed

def test_assembler_BasicOperations():
    assembler = Assembler()
    with open("exercise_1/basicOp.as", "r") as f:
        assembly_code = f.readlines()
    expected_output = ["000002", "050102", "020006", "020007", "00000a", "000001"]
    assert assembler.assemble(assembly_code) == expected_output

#def test_assembler_MemoryOperationsBranch():
#    assembler = Assembler()
#    with open("exercise_1/basicOp.as", "r") as f:
#        assembly_code = f.readlines()
#    expected_output = ["000002", "050102", "020006", "020007", "00000a", "000001"]
#    assert assembler.assemble(assembly_code) == expected_output

#def test_assembler_CopyPrintMemory():
#    assembler = Assembler()
#    with open("exercise_1/basicOp.as", "r") as f:
#        assembly_code = f.readlines()
#    expected_output = ["000002", "050102", "020006", "020007", "00000a", "000001"]
#    assert assembler.assemble(assembly_code) == expected_output


