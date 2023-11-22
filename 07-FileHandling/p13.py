with open("text.txt") as file:
    for x in file:
        print(x, end="")
    file.close()