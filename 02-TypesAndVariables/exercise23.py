import math
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
p=(a+b+c)/2
print(f"area of triangle: {math.sqrt(p*(p-a)*(p-b)*(p-c))}")
print(f"circumference of triangle: {a+b+c}")
