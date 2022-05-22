n=int(input("enter your name:"))
rever=0
while n>0:
    rever=(rever*10)+n%10
    n=n//10
print("rever",rever)



