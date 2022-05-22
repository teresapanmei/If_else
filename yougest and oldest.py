 a=int(input("enter the first age"))
# b=int(input("enter the second age"))
# c=int(input("enter the third age"))
# if a>b and a>c:
#     print("december 31 days")
#     print(a,"a is older")
# elif a<b and a<c:
#     print(a,"b is youngest")
# if b>a and b>c:
#     print(b,"b is oldest")
# elif b<a and b<c:
#     print(b,"b is youngest")
# if c>a and c>b:
#     print(c,"c is oldest")
# elif c<a and c>b:
#     print(c,"c is youngest")
# else:
#     print("error")


a=int(input("enter the number")) 
b=int(input("enter the number")) 
c=int(input("enter the number")) 
if a<b and b<c:
    print(a,"is the youngest",b,"younger",c,"is young")
elif a<b and c<b:
    print(a,"is the youngest",c,"is younger",b,"is young")
elif b<a and a<c:
    print(b,"is the youngest",a,"is younger",c,"is young")
elif b<c and c<a:
    print(b,"is the youngest",c,"is younger",a,"is young")
elif c<b and b<a:
    print(c,"is the youngest",b,"is younger",a,"is young")
elif c<a and a<b:
    print(c,"is the youngest",a,"is younger",b,"is young")
else:
    print("one or both condition are equal")
