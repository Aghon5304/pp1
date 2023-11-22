file = open("countries.txt","r")
numer=1
for line in file:
    print(numer,". ",line, end="")
    numer+=1
file.close()