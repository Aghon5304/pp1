def f(subjects):
    max= 0
    max_name=""
    for przedmiot,oceny in subjects.items():
        srednia = 0
        for x in oceny:
            srednia+=x
        srednia=srednia/len(oceny)
        if srednia>max:
            max = srednia
            max_name=przedmiot
    return max_name

if __name__=="__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))