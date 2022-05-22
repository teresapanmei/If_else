c# ATM question in if else:                                                                                                                                                                                                                           print("ATM programm")
print("WELCOME TO my bank ")
print("swipe your card hear")
atm_pin=9999
transaction = ["balance enqary","withdraw money","diposit","change your pin","tranfer money","quite"]
pin=int(input("enter your pin number"))
if pin==atm_pin:
    print("choose your transaction")
    print("balance enqary")
    print("withdraw money")
    print("diposit")
    print("change your pin")
    print("transfer money")
    print("quite")
    trans = input("enter your transation")
    if trans=="balance enqary":
        sleep=input("Do you want swipe ?")
        if sleep=="yes":
            print("Here is your swipe!, thanks for useing state bank of india ATM")
        else:
            print("thanks for useing state bank of india ATM")
    elif trans=="withdraw money":
        amount=int(input("enter your amount proceeds"))
        if amount>0:
            print("collect your cash , and thanks for using state bank of india")
        else:
            print("Enter your valid amount to proceeds")
    elif trans=="diposit":
        diposit=int(input("Enter your deposits"))
        if diposit>0:
            print("your deposit is done sucsessfully,and thanks to useing state bank of india")
        else:
            print("Enter valid deposits to proceeds")
    elif trans=="change your pin":
        change_pin=int(input("Enter new pin hear"))
        if change_pin>=0:
            print("your pin is change sucsessfully , and thanks for using state bank of india")
        else:
            print("please enter valid pin number")
    elif trans=="transfer money":
        transfer_money=input("enter amount to transfer")
        if transfer_money>0:
            print("your money has been transfered and ,thanks for using state bank of india")
        else:
            print("please enter valid amount to proceeds")
    elif trans=="quite":
        quite=input("enter yes if you want to quite")
        if quite=="yes":
            print("quite")
        else:
            print("choose any transaction please")
else:
    print("wrong pin , try again")