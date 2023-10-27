'''(p6.py) Create a function f(number, even) that computes the sum of the digits of a number. 
When the value of the even parameter is True, the function returns the sum of the even digits. 
When the value of the even parameter is False, the function returns the sum of the odd digits. 
Example:
f(3124,True) returns 6
f(3124,False) returns 4
f(20576,False) returns 12
f(20576,True) returns 8
f(13115,True) returns 0
'''
def f(liczba, ktore):
    suma=0
    if(ktore == True):
        for x in str(liczba):
            x = int(x)
            if(x%2==0):
                suma+=x
    else:
        for x in str(liczba):
            x=int(x)
            if(x%2!=0):
                suma+=x
    return suma

if __name__=="__main__":
    print(f(3124,True) )
    print(f(3124,False))
    print(f(20576,False))
    print(f(20576,True))
    print(f(13115,True))