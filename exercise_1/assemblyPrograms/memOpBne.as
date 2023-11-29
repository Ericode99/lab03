# Program 4: Memory Operations and Branching (Not Equal)
# Demonstrates: str, ldr, bne
ldc R0 10    # R0 = 10 (Memory Address)
ldc R1 20    # R1 = 20
str R1 R0    # Store 20 at address R0 (10)
ldr R2 R0    # Load from address R0 (10) to R2
bne R2 @skip  # Branch if R2 != 0
ldc R2 1     # R2 = 1
prr R2       # Print R2 (will not occure) 
skip:
prr R2       # Print R2 (20)
hlt          # Halt