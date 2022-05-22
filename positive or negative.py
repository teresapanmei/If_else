# user=int(input("enter any number"))
# if user>0: 
#     print("positive")
# elif user<0:
#     print("negative")
# else:
#     print("zero")

# user=int(input("enter the number"))
# if user>0 or user<0:
#     print(-(user))
# else:
#     print("nothing")

# if ("true"):
#     print("teresa")
# elif ("true"):
#     print("o")
# elif ("false"):
#     print("y")
# elif ("true"):
#     print("u")
# else:
#     print("f") 

user=int(input("enter no.:"))
if user>=0:
    print("positive")
    if user%2==0:
        print("divisible")
    else:
        print("not divisible")
else:
    print("negative")
    if user%2!=0:
        print("not divisible")
    else:
        print("divisible")