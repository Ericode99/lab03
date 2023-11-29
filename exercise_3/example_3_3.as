# make the array [1, 2, 3, 4, 5]
# - R0: array base address
# - R1: array length
# - R2: temporary
# - R3: temporary
# - R4: first address
# - R5: last address
ldc R0 35
ldc R1 5
cpy R4 R0

# Create the array [1, 2, 3, 4, 5] in memory starting at line 35
ldc R3 1
str R3 R4
inc R4
inc R3

str R3 R4
inc R4
inc R3

str R3 R4
inc R4
inc R3

str R3 R4
inc R4
inc R3

str R3 R4

# Prepare the registers for the reversing loop
cpy R4 R0
cpy R5 R0
add R5 R1
ldc R1 2
dec R5

# Loop that reverses the array in place
loop:
ldm R2 R4
ldm R3 R5
str R3 R4
str R2 R5
inc R4
dec R5

dec R1
bne R1 @loop
hlt