a = int(input("a: "))
a_max=a
b = int(input("b: "))

while a>0:
    result=""
    if a==1 or a==a_max:
        for x in range(b):
            result+="*"
    else:
        result+="*"
        for x in range(b-2):
            result+=" "
        result+="*"
    print(result)
    a-=1