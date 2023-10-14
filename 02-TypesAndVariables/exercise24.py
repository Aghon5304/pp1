registration = input("enter vechicle registration number: ")
Is_krakow=False
if registration[0]=="K" and registration[1] == "R" or registration[0]=="K" and registration[1] == "K":
    Is_krakow=True
print(f"Car from Kraków: {Is_krakow}")