import random
arr1=[3,7,1,0,4]
arr2=[[2,3],[7,1],[0,4]]
arr3=[7]
for i in range(5):
    arr3.append(i)
arr4 = []
for i in range(1,10):
    arr4.append(i)
arr5=[]
for i in range(1,10):
    arr5.append(i*2)
arr6=[]
for i in range(1,10):
    arr6.append(random.randint(1,20))
arr7 = []
for i in range(5):
    arr7.append([])
arr8=[]
for i in range(4):
    arr8.append([])
    for x in range(2):
        arr8[i].append(x)
arr9=[]
for i in range(5):
    arr9.append([])
    for x in range(3):
        arr9[i].append(
            random.randint(1,20)
        )
arrj=[4,0,3]
arrk=[]
for x in range(15):
    arrk.append(0)
arrl=[]
for x in range(1,31):
    arrl.append(x)
arrm=[]
for x in range(20):
    arrm.append(random.randint(0,1))
arrn=[]
for row in range(5):
    arrn.append([])
    for elem in range(2):
        arrn[row].append(False)
print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)