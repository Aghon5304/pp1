"""45.	An expression contains operators for adding and subtracting single-digit numbers. Define a function f(expression) that returns the value of the expression. Sample result:
"""
def f(expresion):
    a=""
    result=int(expresion[0])
    for x in expresion:
        if(a=="+"):
            result+=int(x)
        elif(a=="-"):
            result-=int(x)
        a=x
    return result


if __name__=="__main__":
    print(f("3+8+1"))