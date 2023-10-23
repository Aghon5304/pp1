number=1
while number<=5:
    result=""
    for x in range(number):
        result+="*"
    print(result)
    number+=1
while number<10:
    result=""
    for x in range(10-number):
        result+="*"
    print(result)
    number+=1
