arr=[-15, 8, -31, 47, -2, 19]
max=arr[1]
min=arr[1]
for x in arr:
    if x>max:
        max = x
    if x<min:
        min=x
print(arr)
print(max)
print(min)