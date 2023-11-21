# Program 2: Memory Operations and Branching
# Demonstrates: str, ldr, beq, bne
ldc R0 10    # R0 = 10 (Memory Address)
ldc R1 20    # R1 = 20
str R1 R0    # Store 20 at address R0 (10)
ldr R2 R0    # Load from address R0 (10) to R2
beq R2 @skip # Branch if R2 == 0
ldc R3 1     # R3 = 1
bne R3 @end  # Branch if R3 != 0
skip:
ldc R3 2     # R3 = 2
end:
prr R3       # Print R3
hlt          # Halt