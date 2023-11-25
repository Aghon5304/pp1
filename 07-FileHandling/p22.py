import re 
file = open("studnets.csv")
table=[]
for line in file:
    line = re.sub("\n","",line)
    numbers  = re.findall('\d{2}', line)
    if(len(numbers)!=0):
        if(int(numbers[-1])<30):
            table.append(re.split(",",line))
lp = 0
for x in range(len(table)):
    print(f"{table[x][0]}   {table[x][1]}   {table[x][4]}")
file.close()
