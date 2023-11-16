'''9.	An array contains values: 2, 3, 7, 5, 4. Create a program that displays:
a.	the array
b.	number of elements
c.	first value
d.	second value
e.	last value
f.	last but one value (do not use negative index values)
g.	sum of the first and last value
h.	middle value
i.	all array values separated by a single space (use a loop statement)
Sample result:
Array: [2,3,7,5,4]
No. of elements: 5
First value: 2
Second value: 3
…
…
Tip: to read the last value of an array:
array[len(array)-1] or array[-1]'''

arr=[2,3,7,5,4]
#a)
print(arr)
#b)
print(len(arr))
#c
print(arr[0])
#d)
print(arr[1])
#e)
print(arr[-1])
#f)
print(arr[len(arr)-2])
#g)
print(int(arr[0])+int(arr[-1]))
#h)
print(arr[len(arr)//2])

print(f"Array: {arr}\nNo. of elements: {len(arr)}\nFirst value: {arr[0]}\nSecond value: {arr[1]}\nLast value: {arr[-1]}\nLast but one: {arr[len(arr)-2]}")
print(f"Sum of first and last: {int(int(arr[0])+int(arr[-1]))}\nMiddle number: {arr[len(arr)//2]}")