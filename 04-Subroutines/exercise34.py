"""34.	Define the function f(n), which returns numbers from 1 to n as a string. Sample result:"""
def f(n):
    result=""
    for x in range (1,n+1):
        result+=str(x)
    return result

if __name__=="__main__":
    print(f(30))