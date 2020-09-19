#PROGRAM TO PRINT STARS IN HEART SHAPE. for input given by the user.
# enter a number:10
#     *         *
#    * *       * *
#   * * *     * * *
#  * * * *   * * * *
# * * * * * * * * * *
# * * * * * * * * * *
#  * * * * * * * * *
#   * * * * * * * *
#    * * * * * * *
#     * * * * * *
#      * * * * *
#       * * * *
#        * * *
#         * *
#          *
num=int(input("enter a number:"))
n=num//2
for row in range(n):
    for col in range(n-row-1):
        print(" ",end="")
    for col in range(row+1):
        print("* ",end="")

    for col in range(2*(n-row-1)):
        print(" ",end="")
    for col in range(row+1):
        print("* ",end="")
    print()

for row in range(num,0,-1):
    for col in range(num-row):
        print(" ",end="")
    for col in range(row,0,-1):
        print("* ",end="")
    print()
