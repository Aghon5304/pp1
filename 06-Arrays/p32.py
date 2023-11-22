def occurs(number,array):
    for x in array:
        if x == number:
            return True
    return False

arr1=[15, 38, 7, 23, 14]

print(occurs(31,arr1))