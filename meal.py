# meal=input("enter the meal:")
# if meal=="breakfast":
#      print("edli")
# if meal=="lunch":
#      print("rice and food")
# if meal=="snacks":
#      print("biscit")
# if meal=="dinner":
#      print("dal")
# if meal=="drinks":
#      print("milk")
# else:
#     print("bye")


# month=int(input("enter the month"))
# if month==1:
#     print("january 31 days")
# elif month==2:
#     print("febuary 28 days")
# elif month==3:
#     print("march 31 days")
# elif month==4:
#     print("april 30 days")
# elif month==5:
#     print("may 31 days")
# elif month==6:
#     print("june 30 days ")
# elif month==7:
#     print("july 31 days")
# elif month==8:
#     print("august 31 days")
# elif month==9:
#     print("september 30 days")
# elif month==10:
#     print("october 31 days")
# elif month==11:
#     print("november 30 days")
# elif month==12:
#     print("december 30")
# else:
#     print("error")

day=input("enter the day")
meal=input("enter the meal") 
if day=="monday":
    if meal=="breakfast":
        print("edli")
    elif meal=="lunch":
        print("rice")
    elif meal=="dinner":
        print("dal")
elif day=="tuesday":
    if meal=="breakfast":
        print("pori")
    elif meal=="lunch":
        print("rice")
    elif meal=="dinner":
        print("dal")
else:
    print("not included")
