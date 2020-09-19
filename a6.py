

# PROGRAM TO PRINT STARS IN PYRAMID SHAPE.
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

def pyramid(rows):
    for i in range(rows):
        print(" "*(rows-i-1)+"* " *(i+1))
    for j in range(rows-1,0,-1):
        print(" "*(rows-j)+"* " *(j))
num=int(input("enter a rows:"))
pyramid(num)


# METHOD 2
# PROGRAM TO PRINT STARS IN PYRAMID SHAPE.
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

def piramid(rows):
    for i in range(rows):
        print(" "*(rows-i-1)+"* "*(i+1))
    for j in range(rows):
        print(" "*(j+1)+"* "*(rows-j-1))

piramid(5)

# METHOD 3
# PROGRAM TO PRINT STARS * IN DIAMOND SHAPE
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     *

def piramid(num):
    for row in range(0,num):
        for col in range(0,num-row-1):
            print(end=' ')
        for col in range(0,row+1):
            print("*",end=" ")
        print()

    for row in range(0,num):
        for col in range(0,row+1):
            print(end=' ')
        for col in range(0,num-row-1):
            print("*",end=" ")
        print()
num=int(input("enter a number:"))
piramid(num)
