unit=int(input("enter the unit"))
if unit>0 and unit<=50:
    total_unit=unit*0.50
    print("electricity bill",total_unit)
elif unit>50 and unit<100:
    total_unit=50*0.50+unit*0.75
    print("electricity bill",total_unit)
elif unit>100 and unit<=250:
    total_unit=50*0.50+100*0.75=unit*1.20
    print("electricity bill",total_unit)
elif unit>250:
    total_unit=50*0.50+100*0.75+250*1.50+0.2
    print("electricity bill",total_unit)
else:
    print("electricity bill",unit)