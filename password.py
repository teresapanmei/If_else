password=input("enter the password") 
if len(password)>1:
    if"$" in password or"@" in password or"#" in password or"&" in password or"^" in password or"!" in password or"`" in password:
        if "0"or"9"in password:
            if"A"or"Z"in password:
                if"a"or"z"in password:
                    print("strong password")
                else:
                    print("weak password")
            else:
                print("weak password")
        else:
            print("weak password")
    else:
        print("weak password")
else:
    print("nothing")
