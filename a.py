print("apka sawagt hai state bank of India") 
print("apna card yaha dale")
ATM_PIN=1234
lenden=("rashi jachana","rashi nikalna","jama karna","apna pin badale","rashi bhejana","bahar")
pin=int(input("apna pin number dale"))
print(" ")
if pin==ATM_PIN:
    print("apna lenden karo")
    print("rashi jachana")
    print("rashi nikalna")
    print("jamakarne")
    print("apna pin badle")
    print("rashi bhejna")
    print("bahar")
    lenden=input("apna leneden kare")
    if lenden ==("rashi jachna"): 
        jamakarne = input("apni rashi jama kare")
    if jamakarne =="jamakarane":
        print("apki rashi jama ho gayi hai")
    else:
        ("apni rashi dale") 
        
        badle_pin=int(input("aapna pin no. daale"))
        if badle_pin>=0:
            print("aapka pin no. safalapurwak badal gya h ,,,, dhanyawaad aapka atm istemaal krne k liye ")
        else:
            print("apka pin manya nahhi hai")
    lendenrashi=input("aapni rashi bheje")
    if lendenrashi>0:
        print("aapki rashi bhej di gayi") 
    else:      
        print("krapya manya rashi dale")
    if lendenrashi=="bahar":
        print("bahar")
else:
        print("pin galat hai dubar koshish kadr")  

     




    