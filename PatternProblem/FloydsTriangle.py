# Q. WAP to print following output.

#        1
#        2 3
#        4 5 6
#        7 8 9 10


# __main__

count=1
for j in range(1,5):

     for i in range(0,j):
           print(count,end=" ")
           count=count+1
     print()