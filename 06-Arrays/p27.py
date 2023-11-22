arr=[12, 6, 4, 9, 10]
def star(n):
    result=""
    for x in range(n):
        result+="*"
    return result
for x in arr:
    print(f"{x}: {star(x)}")
