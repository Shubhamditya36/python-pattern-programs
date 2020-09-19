#PROGRAM T PRINT * IN  REVERSE PYRAMID SHAPE
# * * * *
#  * * *
#   * *
#    *


num=int(input("enter a number of rows:"))
for i in range(0,num):
    for j in range(0,i+1):
        print(end=" ")
    for j in range(0,num-i-1):
        print("*",end=" ")
    print()

# METHOD 2

def pyramid(rows):
    for j in range(rows-1,0,-1):
       print(" "*(rows-j)+"* " *(j))
num=int(input("enter a rows:"))
pyramid(num)
