"""43.	A text contains any number of words. Define a function f(name) that returns the acronym (first letters of all words). Sample result:"""
def f(name):
    a=""
    result=name[0]
    for x in name:
        if a == " ":
            result+=x
        a=x
    return result

if __name__=="__main__":
    print(f("For Your Information"))