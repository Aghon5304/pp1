arr = [2, 3, 2, 5, 8, 1, 9, 8]
bylo = []
wynik=[]
for x in range(len(arr)):
    for y in range(x+1,len(arr)):
        if arr[x]==arr[y]:
            bylo.append(arr[x])

for x in arr:
    czy_bylo=True
    for y in bylo:
        if x==y:
            czy_bylo=False
    if czy_bylo:
        wynik.append(x)

print(arr)
print(wynik)