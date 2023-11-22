file = open("online.txt","r")
dlugosc=0
for x in file:
    dlugosc+=1
file.close()
file = open("online.txt","r")
while dlugosc>-5:
    for x in range(5):
        print(file.readline(),end="")
    if(dlugosc>=5):
        input("Press Enter")
    dlugosc-=5
file.close()