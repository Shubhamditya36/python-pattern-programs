# PROGRAM TO PRINT FLOYD'S TRIANGLE (PRINTING NUMBERS IN RIGHT TRIANGLE SHAPE)
# EXAMPLE :
#
# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1
#



n=int(input("enter a number:"))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(col,end=" ")

    print()
