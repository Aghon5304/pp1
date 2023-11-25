file = open("liczby.txt","w")
for x in range(1,51):
    file.write(str(x)+"\n")
file.close()