import re
file = open("26.txt")
text=re.sub("\n","",file.read())
text=re.split(" ",text)
ile_slow=0

for x in text:
    if len(x)>=6:
        ile_slow+=1
        print(f"{x}")
print(f"ilosc slow = {ile_slow}")
file.close()