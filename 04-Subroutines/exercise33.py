"""33.	Define a function f(n) that returns a string of n asterisks, separated by a slash sign. Sample result:"""
def f(n):
    result=""
    for x in range(n):
        if x >=1:
            result+="/"
        result+="*"
    return result

if __name__=="__main__":
    print(f(5))