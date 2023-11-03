"""40.	Define a function f(number) that returns the sum of repeated digits in a number. Sample result:"""
def f(number):
    result=0
    for x in range(1,10):
        count = 0
        for y in str(number):
            if int(y) == x:
                count+=1
        if count>1:
            result+=x*count
    return result


if __name__=="__main__":
    print(f(513553007))
