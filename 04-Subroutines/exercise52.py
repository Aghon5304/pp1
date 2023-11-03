"""52.	Define a function power(x, n) that calculates xn. Apply recursion. Then, calculate 53."""
def pow(x,n):
    if n ==1:
        return x
    else:
        return x*pow(x,n-1)

if __name__ =="__main__":
    print(pow(3,3))