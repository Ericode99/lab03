# Program 3: Memory Operations and Branching (Equal)
# Demonstrates: str, ldr, beq
ldc R0 10    # R0 = 10 (Memory Address)
ldc R1 0    # R1 = 0
str R1 R0    # Store 0 at address R0 (10)
ldr R2 R0    # Load from address R0 (0) to R3
beq R2 @skip # Branch if R2 == 0
ldc R3 1     # R3 = 1
prr R3       # print R3 (will not occure)
skip:
ldc R3 2     # R3 = 2
prr R3       # Print R3 (2)
hlt          # Halt