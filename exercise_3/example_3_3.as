# make the array [1, 2, 3, 4, 5]
# - R0: array base address
# - R1: array length
# - R2: temporary
# - R3: temporary
# - R4: first address
# - R5: last address
ldc R0 35
ldc R1 5

ldc R3 1
str R3 R0
inc R0
inc R3

str R3 R0
inc R0
inc R3

str R3 R0
inc R0
inc R3

str R3 R0
inc R0
inc R3

str R3 R0

sub R0 R1
cpy R4 R0
cpy R5 R0
add R5 R1
inc R4
ldc R1 2

loop:
ldm R2 R4
ldm R3 R5
prr R2
prr R3
prr R4
prr R5
str R3 R4
str R2 R5
inc R4
dec R5

dec R1
bne R1 @loop
hlt