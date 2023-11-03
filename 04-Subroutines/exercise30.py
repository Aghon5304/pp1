def f(number, even):
    result = 0
    if even == True:
        for x in str(number):
            if int(x)%2==0:
                result+=int(x)
    else:
        for x in number:
            if int(x)%2!=0:
                result+=int(x)
    return result

if __name__=="__main__":
    print(f(3124,True)) 
        
