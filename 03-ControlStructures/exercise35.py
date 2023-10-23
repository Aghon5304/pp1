liczba=1
result=""
while liczba <= 30:
    if liczba%3 ==0 and liczba%5 == 0:
        result+="BINGO"
    elif liczba%3 == 0:
        result+="THREE"
    elif liczba%5 == 0:
        result+="FIVE"
    else:
        result+=str(liczba)
    result+=" "
    liczba+=1
print(result)