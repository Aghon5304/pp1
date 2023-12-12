person = {
    "name":"Marek",
    "surname":"Banach",
    "age":25,
    "hobby":["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321", "moblie":"777888999"}
}
print(person)
print(person["name"])
print(person["hobby"])
person["surname"]="Nowak"
print(person["surname"])
person["married"]=not person["married"]
person["gender"]="male"
person["hobby"].append("bicycle")
person["phone"]["workphone"]="313131444"
print(person)