arr1 =[4,36,12,28,9,44,5]
arr2 = [5,1,36]
wynik =[]
for x in arr1:
    czyPowtarzaSie=True
    for y in arr2:
        if x==y:
            czyPowtarzaSie=False
    if czyPowtarzaSie:
        wynik.append(x)
print(arr1)
print(arr2)
print(wynik)