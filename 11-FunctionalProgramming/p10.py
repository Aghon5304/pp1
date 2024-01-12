def avg_speed(distance,hours,minutes):
    return (distance*60)/(hours*60+minutes)
distance = int(input("enter distance:"))
hours = int(input("enter hours:"))
minutes = int(input("enter minutes:"))

print (avg_speed(distance,hours,minutes))