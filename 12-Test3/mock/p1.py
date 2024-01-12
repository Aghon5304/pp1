
def f(n):
    liczba = f"{n}"
    liczby=[]
    for x in liczba:
        if int(x)%2!=0:
            liczby.append(int(x))
    if(len(liczby)==0):
        return -1
    else:
        max=liczby[0]
        min=liczby[0]
        for x in liczby:
            if x >max:
                max = x
            if x< min:
                min = x
        return max-min
    

print(f"10852: {f(10852)}")
print(f"4388: {f(4388)}")