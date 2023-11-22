arr=[34,7,19,4,21,8]
even=0
while len(arr)>0:
    if arr[-1]%2==0:
        even+=1
    arr.pop()
print(even)