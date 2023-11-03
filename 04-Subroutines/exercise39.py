"""39.	A sentence is an ordered group of words separated by spaces (spaces). Define a function f(sentence) that returns a sentence with spaces removed. Sample result:"""
def f(sentence):
    result=""
    for x in sentence:
        if x !=" ":
            result+=x
    return result


if __name__=="__main__":
    print(f("integrated development environment")  )