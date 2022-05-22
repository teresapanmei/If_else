guess=int(input("enter your number:"))
i=0
chance=5
while i<=5:
    n=int(input("enter your number:"))
    if n==guess:
        print("shivangi, congartulation your winnner")
        break
    else:
        print("you have chance")
    i=i+1
    chance=chance-1
    print("sorry you have only",chance,"chance")     