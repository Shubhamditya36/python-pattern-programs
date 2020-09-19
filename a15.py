# PROGRAM TO PRINT NUMBERS IN HEART SHAPE.

#   * *   * *
# * * * * * * *
# * * * * * * *
#   * * * * *
#     * * *
#       *




for row in range(6):
    for col in range(7):
        if (row==0 and col%3!=0)  or (row==1)or (row==2 ) or ( row==3 and col!=0 and col!=6) or (row==4 and col>1 and col<5) or (col==3 and row>4 ):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
