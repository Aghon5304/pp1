"""46.	Define the function f(x,y), which returns the sum of numbers in the range <x,y> that are completely divisible by 2 and 3 and not divisible by 4. Sample result:"""
def f(x,y):
    result=0
    for x in range(x,y+1):
        if x%2==0 and x%3==0 and x%4!=0:
            result+=x
    return result

if __name__=="__main__":
    print(f(1,20))