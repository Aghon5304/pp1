def phone_keyboard():
    keyboard=""
    for x in range(0,7,3):
        for y in range(1,4):
            keyboard+=str(x+y)+" "
        keyboard+="\n"
    return keyboard

print(phone_keyboard())