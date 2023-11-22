file_name=input("Podaj nazwe pliku: ")
with open(file_name) as file:
    wynik=0
    for x in file:
        wynik+=1
    file.close()
print(wynik)