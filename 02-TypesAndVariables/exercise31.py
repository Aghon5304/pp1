import random
dice = random.randint(1,6)
guess= input("choose a number: ")
print(f"Your guess: {guess==dice}")
