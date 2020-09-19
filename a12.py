# PROGRAM TO PRINT FLOYD'S TRIANGLE (PRINTING STRINGS IN RIGHT TRIANGLE SHAPE)
# EXAMPLE :

# P Y T H O N
# Y T H O N
# T H O N
# H O N
# O N
# N


m=str(input("enter a string :"))
n=len (m)
for row in range(n,0,-1):
    for col in range(0,row):
        print(m[col-row],end=" ")
    print()
