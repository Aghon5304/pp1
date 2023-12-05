phone = {
    "number":"123456",
    "age":5,
    "producent":"nokia",
    "siec": {"5g":"2GB/s","lte":"23mb/s"},
    "stan baterii":"67%",
    "kolory":["czarny","biały","szary"],
    "system":"android 10"
}
for key,Value in phone.items():
    print(f"{key} : {Value}")