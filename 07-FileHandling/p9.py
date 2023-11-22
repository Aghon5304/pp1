file = open("numbers.txt","r")
wynik=0
for line in file:
    wynik+=int(line)
    print(line,end="")
print(wynik)
file.close()