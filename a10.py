# PROGRAM TO PRINT FLOYD'S TRIANGLE (PRINTING STRINGS IN RIGHT TRIANGLE SHAPE)
# EXAMPLE :
#
# P
# Y Y
# T T T
# H H H H
# O O O O O
# N N N N N N

m=str(input("enter a number :"))
n=len (m)
for row in range(n):
    for col in range(0,row+1):
        print(m[row],end=" ")
    print()

