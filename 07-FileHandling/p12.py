file = open("shopping_list.txt","a")
file.write(f"\n{input('Nowy przedmiot na liście: ')}")
file.close()