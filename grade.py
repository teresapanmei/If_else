che=int(input("enter the marks"))
phy=int(input("enter the marks"))
bio=int(input("enter the marks"))
maths=int(input("enter the marks"))
comp=int(input("enter the marks"))
total=che+phy+bio+maths+comp
per=(total/500)*100
print("per=",per)
if per>90:
    print("grade","A")
elif per>80:
    print("grade","B")
elif per>70:
    print("grade","C")
elif per>60:
    print("grade","D")
elif per>50:
    print("grade","E")
else:
    print("grade","F")
