"""42.	Define the function f(number1,number2,number3), which returns the difference between the largest and smallest numbers. Sample result:"""
def f(number1,number2,number3):
    if number1>number2 and number1>number3:
        if number2>number3:
            return number1-number3
        else:
            return number1-number2            
    elif number2>number1 and number2>number3:
        if number1>number3:
            return number2-number3
        else:
            return number2-number1
    else:
        if number1>number2:
            return number3-number2
        else:
            return number3-number1
        
if __name__=="__main__":
    print(f(7,4,9))