'''29.	The vending machine accepts 1, 2 and 5 PLN coins. Define a function f(amount_to_pay) that returns the minimum number of coins that can be used to pay for the purchased product. Sample result:'''
def f(money):
    result=0
    while(money>0):
        if money-5 >=0:
            result+=1
            money-=5
        elif money-2 >=0:
            result+=1
            money-=2
        elif money-1 >=0:
            result+=1
            money-=1
    return result
