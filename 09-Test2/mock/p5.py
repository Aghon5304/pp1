import re
def f(first_letter,last_letter):
    data = open("data.txt","r",encoding="utf8")
    text = data.read()
    count = re.findall(f" {first_letter}[a-zA-Z]*{last_letter} ",text )
    count = len(count)
    data.close()
    return count

if(__name__ == "__main__"):
    print(f("w","d"))