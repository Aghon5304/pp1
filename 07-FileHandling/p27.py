import re
file = open("grades.txt").read()
text = re.sub("(Name: )","",file)
text = re.sub("(Grades: )","",text)
imie = re.findall("^\D.+",text)
imie = imie[-1]
ocena = re.findall("\d.\d",text)
srednia=0
for x in ocena:
    srednia+=float(x)
srednia= srednia/len(ocena)
print(text)
print(imie)
print(ocena)
print(srednia)