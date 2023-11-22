film_titles = ["Władzca Pierścieni","Kapitan Ameryka","Spider-Man","Minionki","Pięć koszmarnych nocy"]
file = open("filmy.txt","w")
for x in film_titles:
    file.write(f"{x} \n")
file.close