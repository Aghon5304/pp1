money = int(input("Enter the amount in PLN: "))
piec = 0
dwa = 0
jeden = 0
while money-5>=0:
    piec+=1
    money-=5
while money-2>=0:
    dwa+=1
    money-=2
while money-1>=0:
    jeden+=1
    money-=1
print(f"The amount of PLN 18 in coins:\n5zł - {piec}\n2zł - {dwa}\n1zł - {jeden}")