"""31.	Define the function f(x,y) that returns the number of negative even numbers in the range <x,y>. Sample result:"""
def f(x,y):
    result=0
    for x in range(x,y+1):
        if x <0 and x%2==0:
            result+=1

    return result

if __name__=="__main__":
    print(f(-7,8))