"""37.	Define the function f(n), which returns the n-th value of the Fibonacci sequence. The sequence is defined as follows: the first value of the sequence is 0, the second value is 1. Each subsequent value is the sum of the previous two. Sample result:"""
def f(n):
    x1=0
    x2=1
    temp=0
    if n >2:
        for x in range(2,n):
            temp=x2
            x2=x2+x1
            x1=temp
        return x2
    elif n ==2:
        return x2
    elif n ==1:
        return x1
        


if __name__=="__main__":
    print(f(5))
    print(f(9))