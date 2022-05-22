i=int(input("enter number  chanck the armstor=="))
a=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if a==sum:
    print("number is Armstrong")
else:
    print("number is not Armstrong")
