#PROGRAM TO PRINT THE PATTERN GIVEN BELOW.

#1
#2 6
#3 7 10
#4 8 11 13
#5 9 12 14 15

num=int(input("enter a number of rows:"))
for row in range (num):
    value=row+1
    dec=num-1
    for col in range(row+1):
        print(value,end=" ")
        value=value+dec
        dec=dec-1
    print()





