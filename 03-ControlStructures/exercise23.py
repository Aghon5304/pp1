human_age=int( input("enter dogs age in human years: "))
age=0
for x in range(1,3):
    human_age-=1
    if(human_age>=0):
        age+=10.5
age+=human_age*4
print(f"The dog's age in dog’s years is {age} years old")