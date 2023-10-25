def diffrent(n1,n2,n3):
    if n1!=n2 and n2!=n3 and n1!=n3 :
        return True
    else:
        return False
    
liczba1 = input("first number: ")
liczba2 = input("second number: ")
liczba3 = input("third number: ")
if diffrent(liczba1,liczba2,liczba3):
    print(f"numbers {liczba1}, {liczba2}, {liczba3} are diffrent")
else:
    print(f"numbers {liczba1}, {liczba2}, {liczba3} are not all diffrent")