user=(input("enter your user"))
age=int(input("enter your age"))
if user=="married":
    if age>=20:
      if age<=40:
        print("hard work")
    else:
        print("no") 
    if age>=40:
      if age<=60:
            if age>=60:
                print("no") 
elif user=="unmarried":
    if age>=15:
     if age<=25:
        print("do study") 
    if age >=25:
        print("do married")  

else:
    print("thank you")     