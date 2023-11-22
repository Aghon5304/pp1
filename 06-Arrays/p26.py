arr=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
max = 0
maxArr=""
for x in arr:
    if max < len(x):
        maxArr=x
        max=len(x)
print(arr)
print(max)
print(maxArr)