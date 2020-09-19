# PROGRAM TO PRINT PATTERN GIVEN BELOW.
#           1
#         2 1 2
#       3 2 1 2 3
#     4 3 2 1 2 3 4
#   5 4 3 2 1 2 3 4 5

num=int(input ("enter a number of rows:"))
for row in range(1,num+1):
    for col in range(0,num-row+1):
        print(end="  ")

    for col in range(row,0,-1):
        print(col,end=" ")

    for col in range(2,row+1):
        print(col,end=" ")
    print()
