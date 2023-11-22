arr=[15, 8, 31, 47, 2, 19]
mean = 0
meanLen= len(arr)
while len(arr)>0:
    mean+=arr[-1]
    arr.pop()
mean=mean/meanLen
print(arr)
print(mean)