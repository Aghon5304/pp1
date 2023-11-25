file=open("powerOfNumber.txt","w")
for x in range(1,11):
    file.write(f"{x},{pow(x,2)},{pow(x,3)} \n")
file.close()