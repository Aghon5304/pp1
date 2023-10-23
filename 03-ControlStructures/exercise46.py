for x in range(1,7):
    result=" "+ str(x)
    for y in range(7,42,7):
        if(x+y<10):
            result+=" "
        result+=" "+str(x+y)
    print(result)