# PROGRAM TO PRINT FLOYD'S TRIANGLE (PRINTING NUMBERS IN RIGHT TRIANGLE SHAPE)
# EXAMPLE :
#
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
#
#

n=int(input("enter a number of rows:"))
for row in range(n,0,-1):
    for col in range(1,row+1):
        print(row,end=" ")
    print()
