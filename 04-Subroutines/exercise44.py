"""44.	A valid password should consist of at least six different characters. Define a function f(password) that returns True if the password is correct or False otherwise. Sample result:"""
def f(password):
    wynik=True
    if len(password)>=6:
        for x in password:
            count=0
            for y in password:
                if x==y:
                    count+=1
                    if count>1:
                        wynik = False
    else:
        return False
    
    return wynik


if __name__=="__main__":
    print(f("qwerty"))