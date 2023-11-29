# Assignment 3

## 1 Unit Testing

#### Documentation

-   **Example**: example text: `example function`.

#### Decisions Taken

**Example**

-   example text: `example function`.

#### Execution

-   the following line has to be executed in the terminal for the code to work with the LGL: `python`

## 2 Disassembler

#### Documentation

-   **Example**: example text: `example function`.

#### Decisions Taken

**Example**

-   example text: `example function`.

#### Execution

-   the following line has to be executed in the terminal for the code to work with the LGL: `python`

## 3 New Features and Problems - Assembler

### 3.1 Increment and Decrement

#### Documentation

-   **inc and dec**: with the instructions inc and dec a register can be increased or decreased by 1. Example syntax: `inc R0`, `dec R0`

#### Decisions Taken

**Added operations to running while loop im vm.py**

-   To ensure the functionality of the extended architecture relevant elif clauses were added to `vm.py` in the while running clause.

#### Execution

-   To run the programm in `example_3_1.as` run the following command in the terminal in the vm/ directory: `python assembler.py ../exercise_3/example_3_1.as ../exercise_3/output_3_1.mx python vm.py ../exercise_3/output_3_1.mx -`

### 3.2 Swap values

#### Documentation

-   **swp**: with the instruction swp two registers will swap values. Syntax is as follows: `swp R1 R2`.

#### Decisions Taken

**Use of temporary variable**

-   In the while running loop in `vm.py` a temporary variable is used to swap the values.

#### Execution

-   To run the programm in `example_3_2.as` run the following command in the terminal in the vm/ directory: `python assembler.py ../exercise_3/example_3_2.as ../exercise_3/output_3_2.mx python vm.py ../exercise_3/output_3_2.mx -`

### 3.3 Reverse Array in Place

#### Documentation

-   **div**: This instruction divides the value of a register by two and applies the Math.floor() function to it -> rounds it to the next lower integer. Syntax: `div R0`

-   **example_3_3.as**: The array [1, 2, 3, 4, 5] gets created at line 35 in memory. Then a loop gets executed to reverse that array. After the program is finished, the reversed array can be found at line 35 in memory. The loop also works with different arrays. To achieve this the user can change the array base address, array length and load a different array into the memeory before the loop.

#### Decisions Taken

**div**

-   This instruction is needed to get the limit of how many times array elements must be exchanged. We could have also introduced an instruction that branches if two register are eqal or the second is smaller than the first register to solve this problem. But we decided to use this div option instead, because one would need to pass 3 registers for the branching solution and that would have needed more changes in the architecture and the assambler.

**Additional registers**

-   Additional registers were added in the `NUM_REG` property of `architecture.py` because they are needed to keep track of all variables in the programm.

**Loop**

-   In order to reverse the array in place a loop is used. The loop counts down from the floored half array length. This is because it needs that many exchanges to reverse the array. Each time the loop is executed, two values at the addresses R4 and R5 (which represent in the first time the loop is executed the `array base address` and `array end address`) are loaded into the two temporary variables R2 and R3. Then R2 is saved at address R5 and R3 is saved at R4, so the values get exchanged. Then R4 is increased by one and R5 is decreased by one. Finally the index R1 is decresed by one. When R1 reaches 0 all array values will have gotten exchanged and the loop will end.

#### Execution

-   To run the programm in `example_3_3.as` run the following command in the terminal in the vm/ directory: `python assembler.py ../exercise_3/example_3_3.as ../exercise_3/output_3_3.mx python vm.py ../exercise_3/output_3_3.mx -`

## 4 New features - Debugger

### 4.1 Show Memory Range

#### Documentation

-   **Example**: example text: `example function`.

#### Decisions Taken

**Example**

-   example text: `example function`.

#### Execution

-   the following line has to be executed in the terminal for the code to work with the LGL: `python`

### 4.2 Breakpoint Addresses

#### Documentation

-   **Example**: example text: `example function`.

#### Decisions Taken

**Example**

-   example text: `example function`.

#### Execution

-   the following line has to be executed in the terminal for the code to work with the LGL: `python`

### 4.3 Command Completion

#### Documentation

-   **Example**: example text: `example function`.

#### Decisions Taken

**Example**

-   example text: `example function`.

#### Execution

-   the following line has to be executed in the terminal for the code to work with the LGL: `python`

### 4.4 Watchpoints

#### Documentation

-   **Example**: example text: `example function`.

#### Decisions Taken

**Example**

-   example text: `example function`.

#### Execution

-   the following line has to be executed in the terminal for the code to work with the LGL: `python`
