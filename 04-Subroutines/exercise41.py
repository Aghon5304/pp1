"""41.	Define the function f(n) that returns the n-th prime number. A prime number is a natural number greater than 1, divisible by 1 and that number. Sample result:"""
def f(n):
    result=2
    now=result
    while(n>1):
        now+=1
        is_prime=True
        for x in range(2,now):
            if now%x == 0:
                is_prime=False
        if is_prime == True:
            result=now
            n-=1
    return result

if __name__=="__main__":
    print(f(5))

