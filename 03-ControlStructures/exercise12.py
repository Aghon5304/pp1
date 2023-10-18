first_firstname=input("first name of first person: ")
first_age=input("age of first person: ")
second_firstname=input("first name of second person: ")
second_age=input("age of second person: ")
if first_age>=18 and second_age>=18: 
    print(f"both {first_firstname} and {second_firstname} are adults")
else:
    print(f"{first_firstname} and {second_firstname} are not adults")