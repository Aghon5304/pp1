pin= "0805"
tries=3
correct_pin=False
while tries>0 and correct_pin==False:
    input_pin=input("Enter the PIN code: ")
    if input_pin==pin:
        correct_pin=True
    else:
        print("Incorrect...")
        tries-=1
if correct_pin==True:
    print("correct pin entered!")
else:
    print("Sorry, your payment card has been blocked.")