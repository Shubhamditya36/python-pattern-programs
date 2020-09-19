#PROGRAM TO PRINT STARS IN HEART SHAPE.
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

for row in range(4):
    for col in range(4-row-1):
        print(" ",end="")
    for col in range(row+1):
        print("* ",end="")

    for col in range(2*(4-row-1)):
        print(" ",end="")
    for col in range(row+1):
        print("* ",end="")
    print()

for row in range(8,0,-1):
    for col in range(8-row):
        print(" ",end="")
    for col in range(row,0,-1):
        print("* ",end="")
    print()
