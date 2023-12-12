import json
movie = {
    "title": "Mr. Bean's Holiday",
    "year": 2007,
    "actor":"Rowan Atkinson",
    "oscar": False,
    "type": "comedy",
}
json.dump(movie,open("favourite.json","w"),indent=3)