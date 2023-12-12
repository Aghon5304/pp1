arr = []
arr.append({
    "name":"Poland",
    "population":39000000,
})
arr.append({
    "name":"Germany",
    "population":84482267
})
arr.append({
    "name":"China",
    "population": 1411750000
})
name = "name"
pop = "population"
print(f"{name:12}     {pop:12}")
for x in arr:
    name = x["name"]
    pop = x["population"]
    print(f"{name:12}   {pop:12}")