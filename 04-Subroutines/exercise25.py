'''25.	Define an anonymous function that returns True when the first number is greater than the second one. Otherwise returns False. Use a conditional operator. Then, check the function for pairs of numbers: 34, 25 and 19,23.'''
def f(a,b):
    if a>b:
        return True
    else:
        return False
    
print(f(34,25))
print(f(19,23))