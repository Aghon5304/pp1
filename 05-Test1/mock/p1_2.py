'''
(p1.py) The vending machine accepts
1, 2 and 5 PLN coins. Define the function
f(amount_to_pay) that returns the minimum number
of coins that can be used to pay
for the purchased product.
'''
def f(amount):
    ile=0
    while amount>0:
        if(amount-5>=0):
            ile+=1
            amount-=5
        elif amount-2>=0:
            ile+=1
            amount-=2
        elif amount-1>=0:
            ile+=1
            amount-=1
    return ile

if __name__=='__main__':
    print(f(23))
    print(f(8))
        
