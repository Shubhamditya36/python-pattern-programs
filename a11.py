# PROGRAM TO PRINT FLOYD'S TRIANGLE (PRINTING STRINGS IN RIGHT TRIANGLE SHAPE)
# EXAMPLE :
# P Y T H O N
# P Y T H O
# P Y T H
# P Y T
# P Y
# P



m=str(input("enter a string :"))
n=len (m)
for row in range(n,0,-1):
    for col in range(0,row):
        print(m[col],end=" ")
    print()
