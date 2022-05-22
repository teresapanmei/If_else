for row in range(7):
    for colum in range(5):
        if (row==0 and colum%4!=0) or (row==3 and colum%4!=0) or (row!=0 and colum==0) or (row%3==0 and colum%4!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
