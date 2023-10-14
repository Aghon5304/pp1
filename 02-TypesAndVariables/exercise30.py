import random
dice = random.randint(1,6)
print(f"dice rolled: {dice}\nSpecial number: {dice==1 or dice == 6}")