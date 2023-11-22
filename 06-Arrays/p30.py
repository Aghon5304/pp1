def bubbleSort(array):
    zmienna=0
    for x in array:
        for y in range(len(array)-1):
            if array[y+1]<array[y]:
                zmienna=array[y+1]
                array[y+1]=array[y]
                array[y]=zmienna
    return array
arr1=[4,36,12,28,9,44,5]
print(arr1)
print(bubbleSort(arr1))