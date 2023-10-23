quantity=0
number=10
sum=0
while number!=0:
    number=int(input("Enter number: "))
    quantity+=1
    sum+=number
quantity-=1
print(f"RESULT: Quantity={quantity}, Sum={sum}, Mean={sum/quantity}")