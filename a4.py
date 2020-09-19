#PROGRAM T PRINT * IN PYRAMID SHAPE
#   *
#  * *
# * * *
#* * * *

num=int(input("enter a number of rows:"))
for i in range(0,num):
    for j in range(0,num-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()


#METHOD 2

def pyramid(rows):
    for i in range(rows):
        print(" "*(rows-i-1)+"* " *(i+1))
num=int(input("enter a rows:"))
pyramid(num)
