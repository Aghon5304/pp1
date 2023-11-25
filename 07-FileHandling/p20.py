import random
file=open("rndNumber.txt","w")
for x in range(50):
    file.write(str(random.randrange(100,999))+"\n")
file.close()