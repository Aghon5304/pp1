import re
liczbaSlow = 1
tekst = "To be, or not to be, that is the question"
spacje=re.findall(" ",tekst)
liczbaSlow += len(spacje)
print(f"{liczbaSlow} {spacje}")