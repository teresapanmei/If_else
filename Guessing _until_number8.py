guess=int(input("guessing your number:"))
i=1
while i<5:
    num=int(input("inter your number:"))
    if guess<num:
        print(" number entered by you entered is samll ,try one more time")
    elif guess>num: 
        print(" your enered is gerater,try one more time ") 
    elif guess==num:
        print("wow you guess")
    else:
        print("chances are finished") 
    i=i+1

# a="5"
# b="shivange"
# c="3.4"
# d=float(c)
# e=int(d)
# print(e,"=",b,',',b,'+',b,',',b,',',b))

# i=1
# j=0
# while i<4:
#     n=int(input("inter your number"))
#     j=j+n
#     print(j,"fibonacci")
#     i=i+1