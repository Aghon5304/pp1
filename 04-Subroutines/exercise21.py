import mymath,mykeyboard
a= mykeyboard.read_number()
b= mymath.generate_number()
print(f"Computer number: {b}")
if a==b:
    print("You Won The Game!!!!")
else:
    print("You lost The Game!!!!")