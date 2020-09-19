# PROGRAM TO PRINT FLOYD'S TRIANGLE (PRINTING NUMBERS IN RIGHT TRIANGLE SHAPE)
# EXAMPLE :
#
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5

n=int(input("enter a number of rows:"))
num=1
for row in range(n,0,-1):
    for col in range(0,row):
        print(num,end=" ")
    num+=1
    print()
