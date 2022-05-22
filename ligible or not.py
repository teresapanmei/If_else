age=int(input("enter the age:"))
sex=input("enter sex f or m:") 
status=input("enter status y or n:")
if sex=="F":
    if status=="y":
        print("will work in urban areas")
    else:
       print("she will not work")
elif age>20 and age<40:
        if sex=="m":
            if status=="y":
                print("he may work in anywhere")
            else:
                print("error")
elif age>40 and age<60:
    if sex=="m":
        if status=="y":
            print("he will work in urban areas")
        else:
            print("he can't work")
else:
    print("invalid")
