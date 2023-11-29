# Program 2: Copy and Print Memory
# Demonstrates: cpy, prm, ldc, str, hlt
ldc R0 30    # R0 = 30 (Memory Address)
ldc R1 99    # R1 = 99
str R1 R0    # Store 99 at address R0 (30)
cpy R2 R0    # R2 = R0 (30)
prm R2       # Print memory[R2] (99)
hlt          # Halt