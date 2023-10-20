ean=input("Enter EAN-13 article number: ")
if len(ean)==13:
    print("Article number is correct")
    if ean[0,2] == "590":
        print("Article is manufactored in Poland")
    else:
        print("not manufactored in Poland")
else:
    print("article number in incorrect!")