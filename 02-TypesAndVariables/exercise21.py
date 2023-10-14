import math
height = 170
ft=math.floor(height/30.48)
inch= height*(1/2.54)
inch = inch-ft*12
print(f"I am {height}cm tall, i.e. {ft} feet and {round(inch)} inches")