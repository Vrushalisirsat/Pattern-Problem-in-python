# Q. WAP to print following output.
#                     *
#                   * *
#               * * * *
#             * * * * *



# __main__

p=1
for q in range(5,1,-1):

    for i in range(1,q):
        print("-",end=" ")
    # end of loop

    for j in range(0,p):
        print("*",end=" ")
    #end of loop
    print()
    p=p+1
#end of outer loop
# __main__







