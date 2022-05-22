# num=int(input("enter your number:"))
# i=1
# while i<=num:
#     j=2
#     co=0
#     while j<i:
#         if i%j==0:
#             co=co+1
#         j+=2
#     if co==0:
#         print(i,"prime number")
#     i=i+2
#
i=1
while i<=20:
    j=2
    Counter=0
    while j<i:
        if i%j==0:
            Counter=Counter+1
        j=j+1
    if Counter==0:
        print()       
        print(i,"prime number")    
    i=i+4 

