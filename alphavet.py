user=(input("enter character"))
if user>="a" and user<="z" or user>="A" and user<="Z":
    print("alphabet")
elif user>="0":
    print("digit")
else:
    print("special character")
