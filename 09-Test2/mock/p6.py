import json
def f(years,curse):
    iloscStudentow=0
    file = open("data.json","r")
    table = json.loads(file.read())
    for verse in table:
        if verse["age"] >=years:
            srednia=0
            ile = 0
            for x in verse["studies"]["courses"]:
                if(x["name"]==curse):
                    for liczba in x["grades"]:
                        srednia+=int(liczba)
                        ile+=1
            if ile >0:
                srednia=srednia/ile
            if srednia>=4:
                iloscStudentow+=1
    return iloscStudentow
if __name__=="__main__":
    print(f(21,'statistics'))