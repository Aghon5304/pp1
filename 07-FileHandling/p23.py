import re
daneZInternetu = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatury = re.findall("\d{2}",daneZInternetu)
srednia=0
for x in temperatury:
    srednia+=int(x)
srednia=srednia/3
print(srednia)