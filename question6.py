n=int(input("enter the number="))
i=1
while i<=n:
    i+=2
    if i%3==0:
        j=3
        if j%i==0:
            print(j,"prime number")
        else:
            print(i,"not prime number")
        j+=1
    else:
        print(i,"prime number")
    
    
       
# if "true":
#     print("p")
# else:
#     print("k")

# i=20
# while i<=100:
#     if i%2==0:
#         print(0)
#     i=i+1

