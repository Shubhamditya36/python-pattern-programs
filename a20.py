#PROGRAM T PRINT * IN BELOW GIVEN SHAPE.
#     *
#    *P*
#   *P*P*
#  *P*P*P*
# *P*P*P*P*

num=int(input("enter a number of rows:"))
for i in range(0,num):
    count=0
    for j in range(num-i-1):
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
        if count<i:
            print("P",end="")
            count+=1
    print()
