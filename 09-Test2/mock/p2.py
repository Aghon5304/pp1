def f(arr):
    litery=[]
    litery.append(arr[0])
    count=0
    for x in range(len(arr)):
        if(litery[0]==arr[x]):
            count+=1
        else:
            litery.append(arr[x])
    if count==1:
        return litery[0]
    else:
        return litery[1]

if __name__ == "__main__":
    print(f([6,6,6,63,6,6,6,6,6,6,6,6,6,6,6,6,6,6]))