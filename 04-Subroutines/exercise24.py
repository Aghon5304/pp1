'''24.	In a separate module, define a function that checks if the number is within the range <x, y>. The function returns a boolean value. Then, create a program and use the function you defined. Sample result:
A number: 7
Number 7 in the range <2,15>: yes 
'''
import mod24

if mod24.czy_liczba_w_przedziale(7,2,15):
    print("A number: 7 \nNumber 7 in the range <2,15>")
else:
    print("A number: 7 is not in the range <2,15>")