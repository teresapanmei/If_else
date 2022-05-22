# user=int(input("enter year:"))
# if user%4==0 or user%400==0:
#     print("leap year")
# elif user%4!=0 and user%400!=0:
#     print("not a leap year")
# else:
#     print("error")


# user=int(input("enter the year"))
# if user%4==0:
#     print("leap year")
#     if user%400==0:
#         print("century year")
#     else:
#         print("not century year")
# else:
#     print("not leap") 

user=int(input("enter year"))
if user%4==0:
    print("leap yr")
    if user%100==0:
        print("century")
    else:
        print("not a century")
else:
    print("not a leap yr")




