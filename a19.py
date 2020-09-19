#PROGRAM TO PRINT THE PATTERN GIVEN BELOW.

#1
#2 9
#3 8 10
#4 7 11 14
#5 6 12 13 14 15

num=int(input("enter a number of rows:"))
for row in range (num):
    for col in range(row+1):
        x=0
        for k in range(col):
           x=x+num-k
        if col%2==0:
            print(x+row-col+1,end=" ")
        else:
            print(x+num-row,end=" ")
    print()

    print()





