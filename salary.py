salary=int(input("enter the salary"))
if salary<=10000:
    gross_salary=salary+0.2+0.8
    print("salary of employer",gross_salary)
elif salary<20000:
    gross_salary=salary+0.25+0.9
    print("salary of employer",gross_salary)
else:
    print("salary of employer",salary+0.3+0.95)
