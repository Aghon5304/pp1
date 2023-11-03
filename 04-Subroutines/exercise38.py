"""38.	A palindrome is an expression that sounds the same when read backwards. Define a function f(palindrome) that returns True if the expression is a palindrome or False otherwise. Sample result:"""
def f(palindrome):
    result = True
    a =""
    b =""
    for x in range(0,len(palindrome)):
        if palindrome[x]!=palindrome[-x-1]:
            result=False
    return result


if __name__=="__main__":
    print(f("radar") )
    print(f("12-11-21") )
    print(f("book"))
