# PROGRAM TO PRINT STARS * IN  REVERSE RIGHT ANGLE TRIANGLE SHAPE .
# ****
# ***
# **
# *
num=int(input("enter a number of rows:"))
for i in range(num,0,-1):
    for j in range(0,i):
        print("*",end="")
    print()

