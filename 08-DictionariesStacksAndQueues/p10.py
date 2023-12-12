import json
with open("country-by-population.json") as file:
    data = json.load(file)
key,value=data[0]
print(f"{key:15}    {value:15}")

for x in data:
    for key,value in x.items():
        print(f"{key:15}    {value:15}")