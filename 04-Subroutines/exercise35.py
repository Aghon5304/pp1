"""35.	Two numbers and an operator are given. Define a function f(number1,number2,operator) that returns the result of an arithmetic operation. The available operators are +,-,*,%,**. Sample result:"""
def f(n1,n2,op):
    if op=="+" :
        return n1+n2
    elif op =="-":
        return n1-n2
    elif op == "%":
        return n1%n2
    elif op =="*":
        return n1*n2
    elif op =="**":
        return n1**n2
if __name__=="__main__":
    print(f(2,3, "+"))
    print(f(2,3, "**") )