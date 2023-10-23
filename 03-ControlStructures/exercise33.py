decimal_number=int(input("Enter decimal number: "))
number=decimal_number
bianary=""
while number>0:
    if number%2 ==0:
        bianary+="0"
    else:
        bianary+="1"
    number=int(number/2)
bianary=bianary[::-1]
print(f"{decimal_number}(10) = {bianary}(2)")