import json
stuednt = {
    "title": "Mr. Bean's Holiday",
    "rocznik": 2007,
    "imie":"Rowan",
    "nazwisko":"Atkinson",
    "frekdencja":" 13%",
    "oceny": [5,5,5,5,5,5,5,5,4,1,5],
}
json.dump(stuednt,open("student.json","w"),indent=3)