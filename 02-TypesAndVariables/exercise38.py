numer = input("Enter phone number: ")
new_number=""
for x in range(9):
    new_number+=numer[x]
    if x == 2 or x==5:
        new_number+="-"
print(new_number)