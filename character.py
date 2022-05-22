
cha=input("enter any character")
if cha>="a" and cha <="z" or cha>="A" and cha<="Z":
    print("alphabet")
elif cha>="1" and cha<="9":
    print("digit")
else:
    print("special character")