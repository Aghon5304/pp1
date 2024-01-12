
distance = int(input("enter distance:"))
hours = int(input("enter hours:"))
minutes = int(input("enter minutes:"))
avrg = lambda distance,hours,minutes:distance*60/(hours*60+minutes)
print(avrg(distance,hours,minutes))