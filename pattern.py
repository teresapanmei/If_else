n=6
i=1
while i<=7:
    if i%3==0 and n%3!=0  or i==1 and n%3==0 or i-n==2 or i+n==8:
        print("*",end=" ")
    else:
        print() 
    print()
    i=i+1      
   