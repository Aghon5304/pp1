def f(card_number):
    a=""
    for x in range(11):
        a+="*"
    result=card_number[0:2]+a+card_number[-4:]
    return result
