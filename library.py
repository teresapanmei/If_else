expected_date=int(input("enter the expected_date"))
expected_month=int(input("enter the expected_month"))
expected_year=int(input("enter the expected_year"))
return_date=int(input("enter the return day"))
return_month=int(input("enter the return month"))
return_year=int(input("enter the return year"))
if expected_year==return_year:
    if expected_month==return_month:
        if expected_date==return_date:
            print("no fine")
        else:
            print("cost of book",(return_date-expected_date)*15)
    else:
        print("cost of book",(return_month-expected_month)*500)
else:
    print("cost of the book",(return_year-expected_year)*1000)
