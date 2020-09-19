# PROGRAM TO PRINT FLOYD'S TRIANGLE (PRINTING NUMBERS IN RIGHT TRIANGLE SHAPE)
# EXAMPLE :
#
# 1234
# 567
# 89
# 10



n=int(input("enter a number:"))
num=1
for row in range(n,0,-1):
    for col in range(0,row-1):
        print(num,end="")
        num+=1
    print()
