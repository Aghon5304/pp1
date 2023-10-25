def number(n):
    result = "<1,"+str(n)+">:"
    for x in range(1,n+1):
        result+=" "+str(x)
    return result
print(number(19))