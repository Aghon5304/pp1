card = input("Enter credit card number: ")
new_card=""
for x in range(16):
    new_card+=card[x]
    if x == 3 or x==7 or x==11:
        new_card+=" "
print(f"Card number: {new_card}")