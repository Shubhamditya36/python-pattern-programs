# PROGRAM TO PRINT FLOYD'S TRIANGLE (PRINTING STRINGS IN RIGHT TRIANGLE SHAPE)
# EXAMPLE :
#
# p
# p y
# p y t
# p y t h
# p y t h o
# p y t h o n



m=str(input("enter a string:"))
n=len(m)
for row in range(n):
    for col in range(0,row+1):
        print(m[col],end=" ")
    print()
