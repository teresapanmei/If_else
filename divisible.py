# num=int(input("enter any number"))
# if num%2==0:
#     print("divisible")
# elif num%2!=0:
#     print("not divisible")

user=int(input("enter any number"))
if user>=9:
    print("user is greater")
    if user%3==0:
        print("divisible")
    else:
        print("not divisible")
elif user==9:
    print("user is equal")
    if user%4==0:
        print("divisible")
    else:
        print("not divisible")
else:
    print("user is smaller")