# Assignment 3

## 1 Unit Testing

### Documentation

The tests are written using Python's pytest framework, which had to be installed using `pip3 install pytest` in the terminal. For viewing the test coverage, the addition to pytest was installed using `pip3 install pytest-cov`.

#### test_assembler.py

- **Purpose**: The purpose of the `test_assembler.py` file is to validate the funcionality of the `assembler.py` program, which can be found in the `debugger` and `vm` folder. the assembler converts assembly language instruction (found in folder `exercise_1/assemblyPrograms`) into machine code (found in folder `exercise_1/vmInstructions`). The test in the `test_assembler.py` file ensure that the conversion is correct by targeting each assembly program with a specific test function.

- **subprocess**: All functions first generate the corresponding `.mx` file, because the test need to ensure that the values in those `.mx` files, which were generated by the assembler, are correct.

- **assembler_basic_operation_program (basicOp)**: This test function tests the assembler if it correctly translated the basic arithemetic `virtual machine op-codes` from the assembly program (found in `exercise_1/assemblyPrograms/basicOp.as`) to the virtual machine instructions (found in `exercise_1/vmInstructions/basicOp.mx`). The values in the `.mx` file are then compared to the calculated values in the variable `expected_output`.

- **assembler_print_memory_program (copyPrntMem)**: This test function tests the assembler if it correctly translated the print and memory `virtual machine op-codes` from the assembly program (found in `exercise_1/assemblyPrograms/copyPrntMem.as`) to the virtual machine instructions (found in `exercise_1/vmInstructions/copyPrntMem.mx`). The values in the `.mx` file are then compared to the calculated values in the variable `expected_output`.

- **assembler_memory_operations_branch_equal_program (memOpBeq)**: This test function tests the assembler if it correctly translated the memory and branch equal `virtual machine op-codes` from the assembly program (found in `exercise_1/assemblyPrograms/memOpBeq.as`) to the virtual machine instructions (found in `exercise_1/vmInstructions/memOpBeq.mx`). The values in the `.mx` file are then compared to the calculated values in the variable `expected_output`.

- **assembler_memory_operations_branch_notEqual_program (memOpBne)**: This test function tests the assembler if it correctly translated the memory and branch not equal `virtual machine op-codes` from the assembly program (found in `exercise_1/assemblyPrograms/memOpBne.as`) to the virtual machine instructions (found in `exercise_1/vmInstructions/memOpBne.mx`). The values in the `.mx` file are then compared to the calculated values in the variable `expected_output`.

With these test, it is ensured that **all 11** `virtual machine op-codes` were correctly translated by the assembler.

#### test_vm.py

- **Purpose**: the `test_vm.py` file validates that the functionality of the `vm.py` program located in the `vm` folder is correctly implemented. The VM (virtual machine) executes machine code instruction from the files created by the assembler in the folder `exercise_1/vmInstructions`. The tests in `test_vm.py` ensure that the VM correctly interprets and executes each provided machine code instruction (`.mx` file), generating the expected output. Each test function in this file is dedicated to verifying the VM's output of a specific machine code file. The `.out` files that are generated after executing each `.mx` file are found in the folder `exercise_1/vmOutput`.

- **subprocess**: Just like in the `test_assembler.py` in every test function, subprocess.run is used to execute the VM with the given `.mx` file.

- **vm_basic_operation_program (basicOp)**: This test function checks the VM's capability to handle basic arithmetic operations. It runs the VM with the machine code from `vmInstructions/basicOp.mx` generated by the assembler and compares the output captured from the VM to the expected output defined in the test.

- **vm_print_memory_program (copyPrntMem)**: This function tests the VM's ability to execute instructions related to copying, printing, and memory operations. It runs the VM with the machine code from `vmInstructions/copyPrntMem.mx` generated by the assembler and compares the output captured from the VM to the expected output defined in the test.

- **vm_memory_operations_branch_equal_program (memOpBeq)**: This test function checks the VM's capability to handle memory operations and branch conditions (equal) and memory operations. It runs the VM with the machine code from `vmInstructions/memOpBeq.mx` generated by the assembler and compares the output captured from the VM to the expected output defined in the test.

- **vm_memory_operations_branch_notEqual_program (memOpBne)**: This test function checks the VM's capability to handle memory operations and branch conditions (not equal) and memory operations. It runs the VM with the machine code from `vmInstructions/memOpBne.mx` generated by the assembler and compares the output captured from the VM to the expected output defined in the test.

With these test, it is ensured that the VM correctly executes the given machine codes.

#### test_error.py

- **Purpose**: The `test_error.py` is used to validate the error-handling capabilities of the `vm.py` program located in the `vm` folder. The test functions specifically target scenarios, where VM encounters error conditions such as `out-of-memory` and `invalid instructions`. The tests ensures that the VM does not only detects these errors, but also responds with the appropriate error messages.

- **subprocess**: Each test function within `test_error.py` utilizes `subprocess.run` to execute the VM with the specific `.mx` file that are designed to trigger an error.

- **error_out_of_memory_program**: This test function tests the VM's response to an `out-of-memory` scenario. The VM is executed with a machine code file `out_of_memory.mx`, wich is found in the `errorAssemblyPrograms` folder, intended to exceed its memory capacity. The test verifies that the `AssertionError` with `"Program too long"` is raised.

- **error_invalid_instruction_program**: This test function tests the VM's response to an `invalid instruction` scenario. The VM is executed with a machine code file `invalid_instruction.mx`, wich is found in the `errorAssemblyPrograms` folder, intended to give a not existing instruction to the VM. The test verifies that the `AssertionError` with `"Unknown op"` is raised.

With these tests, it is ensured that the VM handles the two mentioned errors correctly.

### Decisions Taken

**File Structure**

- Pytest allows for a certain amount of freedom in the file structure. For keeping a clean folder in `exercise_1` there were subfolders created for each file ending and a seperate folder for the files raising errors.

**Assembler Test: Simulate Terminal Input**

- **subprocess**: The task stated that each `.as` file had to be run through the assembler for creating its corresponding `.mx` file. Therefore the module `subprocess` was used, to simulate the terminal input for generating the corresponding `.mx` files by the assembler.

**Virtual Machine Test: Simulate Terminal Input and getting Output**

- **subprocess**: The task stated that each `.mx` file had to be run through the VM for generating the output in the terminal. Therefore again the module `subprocess` was used, to simulate how the VM would be run in a real-world scenario by generating the corresponding `.out` files. Since the output in the terminal had to be checked in the test and not values in the `.out` files, the `subprocess.run()` had to be extended with `stdout=subprocess.PIPE`, which allows the output to be captured and then again used by using `.stdout.strip()` to save the output in the variable`generated_output`.

**Error Test: Simulate Terminal Input and getting Output**

- **subprocess**: For simulating a real-world scenario the files `out_of_memory.mx` and `invalid_instruction.mx` were created manually and again executed with the help of `subprocess.run()`. Since the error is seen in the Terminal, the `subprocess.run()` had to be extended with `stderr=subprocess.PIPE`, which allows the error to be captured and then again used by using `.stderr.strip()` to save the error in the variable`generated_error`.

### Execution

- **Pytest**: To test the test-files in `exercise_1`, you have to make sure, that you are in the folder. If not, execute `cd exercise_1` in the terminal. Now execute `pytest` in the terminal.

- **Coverage**: To see the test coverage of the test-files with their corresponding programs that were tested, execute the following in the terminal: `pytest --cov=vm --cov=assembler --cov=test_assembler --cov=test_vm --cov=test_errors`
  Since only the generated files and output were compared in the tests and not the specific functions in the programs, the test-coverage is not really meaningful. An informative and meaningful test-coverage will be seen in task 2.

## 2 Disassembler

### Documentation

#### disassembler.py

- **decode**: The `decode()` function extracts the operation code (`op-code`) and arguments from a single machine code instruction. After, it returns the `op-code` and `two arguments`.

- **disassemble**: The `disassemble()` function converts a single line of machine code into its corresponding assembly language instruction by handling different instruction formats correctly.

- **disassemble_file**: The `disassemble_file()` function processes an entire `.mx` file, converting each line of machine code into assembly language and writing it in the output `.as` file.

#### test_disassembler.py

- **test_disassemble**: The `@pytest.mark.parametrize` allows to write mulitple input and output cases that can then be tested an once in the `test_disassemble()` function.

- **test_disassemble**: This test function simulates an execution of a `.mx` file in the terminal by using `subprocess.run()`. After, it compares the generated `.as` file with the expected output.

### Decisions Taken

**Parametrize**

- To write less test functions the `pytest parametrization` was used. Furthermore, in order to create more significant test coverage, selected functions were tested in the `disassembler.py` file instead of comparing the contents of the generated files.

### Execution

- **Pytest**: To test the test-file in `exercise_2`, you have to make sure, that you are in the folder. If not, execute `cd exercise_2` in the terminal. Now execute `pytest` in the terminal.

- **Coverage**: To see the test coverage of the `test_disassembler.py` with its corresponding program `disassembler.py`, execute the following in the terminal: `pytest --cov=disassembler --cov=test_disassembler`

## 3 New Features and Problems - Assembler

### 3.1 Increment and Decrement

#### Documentation

- **inc and dec**: with the instructions inc and dec a register can be increased or decreased by 1. Example syntax: `inc R0`, `dec R0`

#### Decisions Taken

**Added operations to running while loop im vm.py**

- To ensure the functionality of the extended architecture relevant elif clauses were added to `vm.py` in the while running clause.

#### Execution

- To run the programm in `example_3_1.as` run the following command in the terminal in the vm/ directory: `python assembler.py ../exercise_3/example_3_1.as ../exercise_3/output_3_1.mx python vm.py ../exercise_3/output_3_1.mx -`

### 3.2 Swap values

#### Documentation

- **swp**: with the instruction swp two registers will swap values. Syntax is as follows: `swp R1 R2`.

#### Decisions Taken

**Use of temporary variable**

- In the while running loop in `vm.py` a temporary variable is used to swap the values.

#### Execution

- To run the programm in `example_3_2.as` run the following command in the terminal in the vm/ directory: `python assembler.py ../exercise_3/example_3_2.as ../exercise_3/output_3_2.mx python vm.py ../exercise_3/output_3_2.mx -`

### 3.3 Reverse Array in Place

#### Documentation

- **div**: This instruction divides the value of a register by two and applies the Math.floor() function to it -> rounds it to the next lower integer. Syntax: `div R0`

- **example_3_3.as**: The array [1, 2, 3, 4, 5] gets created at line 35 in memory. Then a loop gets executed to reverse that array. After the program is finished, the reversed array can be found at line 35 in memory. The loop also works with different arrays. To achieve this the user can change the array base address, array length and load a different array into the memeory before the loop.

#### Decisions Taken

**div**

- This instruction is needed to get the limit of how many times array elements must be exchanged. We could have also introduced an instruction that branches if two register are eqal or the second is smaller than the first register to solve this problem. But we decided to use this div option instead, because one would need to pass 3 registers for the branching solution and that would have needed more changes in the architecture and the assambler.

**Additional registers**

- Additional registers were added in the `NUM_REG` property of `architecture.py` because they are needed to keep track of all variables in the programm.

**Loop**

- In order to reverse the array in place a loop is used. The loop counts down from the floored half array length. This is because it needs that many exchanges to reverse the array. Each time the loop is executed, two values at the addresses R4 and R5 (which represent in the first time the loop is executed the `array base address` and `array end address`) are loaded into the two temporary variables R2 and R3. Then R2 is saved at address R5 and R3 is saved at R4, so the values get exchanged. Then R4 is increased by one and R5 is decreased by one. Finally the index R1 is decresed by one. When R1 reaches 0 all array values will have gotten exchanged and the loop will end.

#### Execution

- To run the programm in `example_3_3.as` run the following command in the terminal in the vm/ directory: `python assembler.py ../exercise_3/example_3_3.as ../exercise_3/output_3_3.mx python vm.py ../exercise_3/output_3_3.mx -`

## 4 New features - Debugger

### 4.1 Show Memory Range

#### Documentation

- By typing the command 'm index' or 'm index1 index2' the content of the memory at 'index' respective everything between 'index1' and 'index2'.

#### Decisions Taken

- To make it possible for the user to show the memory at a specific location or a specific range an additional elif statement 
  was added to `interact` in `vm_step.py`. In it the assigned `index` or `index1` and `index2` get tested if they within the memory range, by the newly created function `get_memory_range`
  and then assigned to the named parameters `start` and `stop` of `show`.
- To make it  the above possible, `show` in `vm_base.py` was adjusted so that it has two named parameters `start` and `stop`
  which are both default -1. Depending on the value of `start` and `stop` different behaviour is exhibited.

#### Execution

- To test the newly added functionality run the program in the dictionary `debugger` with the command python3 `vm_step.py count_up.mx`
  and enter the above described commands.

### 4.2 Breakpoint Addresses

#### Documentation

- To set a clear a breakpoint at a given address, use the commands `b index` or `break index` respective 
  `c index` or `clear index`.

#### Decisions Taken

- To set a clear a breakpoint at a given address (`index`), an addtional `elif` statement checking for additional input other than `memory` command, as well as the function `get_index_of_memory` 
  was added. Together they check if `index` is within the memory range and if it is pass it to the already existing
  `_do_breakpoint` respective `_do_clear_breakpoint`.


#### Execution

- To test the newly added functionality run the program in the dictionary `debugger` with the command `python3 vm_break.py count_up.mx`
  and enter the above described commands.

### 4.3 Command Completion

#### Documentation

- The debugger gets modified to recognize commands based on any number of distinct leading characters. For
  example, any of `m`, `me`, `mem`, and so on triggers `do_memory`.

#### Decisions Taken

- To achieve the above, `vm_extend.py` was modified by adding `call_method` which is called in the different cases in `interact`. 
  It iterates over the functions of the class and if the command entered by the user is a prefix of a valid function after the `_do_` prefix
  the given function is called.

#### Execution

- To test the newly added functionality run the program in the dictionary `debugger` with the command `python3 vm_break.py count_up.mx`
  and enter any valid command with any numbers of distinct leading characters. For example: `mem 1 3` to show the memory range from index 1 to 3.

### 4.4 Watchpoints

#### Documentation

- Allows the user to create watchpoints at a given address. If the user specifies a
  watchpoint for address 0x0010, then the VM automatically halts whenever a new value is stored at that
  location.

#### Decisions Taken

- To achieve the desired behaviour `_do_watchpoint` was added to `vm_break.py`. It stores the address of the created watchpoint
  in `watchpoints`. `run` now additionally checks if the current instructions changes the memory where a watchpoint is set. 
  If this is the case the program halts.

#### Execution

- To test the newly added functionality run the program in the dictionary `debugger` with the command `python3 vm_break.py count_up.mx`
  and enter any numbers of distinct leading characters of the command watchpoint with the desired index to set the watchpoint at. 
  For example: `wa 2` to set a watchpoint at address 2.

Task 3 execution:
inside vm folder run:

python assembler.py ../exercise_3/example_3_2.as ../exercise_3/output_3_2.mx
python vm.py ../exercise_3/output_3_2.mx -

python assembler.py ../exercise_3/example_3_3.as ../exercise_3/output_3_3.mx
python vm.py ../exercise_3/output_3_3.mx -

- the following line has to be executed in the terminal for the code to work with the LGL: `python`
