"""47.	Define a function f(text) that returns the given text with all characters separated by "-" (minus sign). Example:"""
def f(text):
    result=text[0]
    text=text[1:]
    for x in text:
        result+="-"+x
    return result

if __name__ =="__main__":
    print(f("University"))