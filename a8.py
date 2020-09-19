# PROGRAM TO PRINT FLOYD'S TRIANGLE (PRINTING NUMBERS IN RIGHT TRIANGLE SHAPE)
# EXAMPLE :
#
# 1
# 22
# 333
# 4444
# 55555


n=int(input("enter a number:"))
num=1
for row in range(0,n):
    for col in range(0,row+1):
        print(num,end="")
    num+=1
    print()
