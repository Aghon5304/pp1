arr=[15, 8, 31, 47, 2, 19]
reversedArray=[]
for x in range(len(arr)):
    reversedArray.append(arr[-(x+1)])
print(arr)
print(reversedArray)