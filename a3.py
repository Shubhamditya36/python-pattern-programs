# PROGRAM TO PRINT STARS * IN RIGHT ANGLE TRIANGLE SHAPE.
# *
# ***
# *****
# *******

num=int(input("enter a number of rows:"))
k=1
for i in range(1,num+1):
    for j in range(1,k+1):
        print("* ",end=" ")
    k+=2
    print()

