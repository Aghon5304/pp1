'''23.	Create a program that calculates how many times the given letter appears in any text. Then create a program and check how many times the letter ‘e’ appears in the text below. In a separate module, define a function for making calculations. Sample result:
You never get a second chance to make a first impression
The number of letter 'e': 7
'''
def wystepowanie_litery(litera,zdanie):
    
    wynik= 0
    for x in zdanie:
        if x==litera:
            wynik+=1
    return wynik

zad="You never get a second chance to make a first impression"
print(wystepowanie_litery("e",zad))