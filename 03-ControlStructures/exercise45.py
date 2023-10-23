number=2
n=int(input("enter N: "))
prime_number=""
result=""
while n>0:
    is_prime=True
    for x in range(2,number):
        if number%x ==0:
            is_prime=False
    if is_prime ==True:
        if number == 2:
            result=str(number)
        else:
            result+=", "+str(number)
        n-=1
    
    number+=1
print(result)