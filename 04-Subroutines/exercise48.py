"""48.	Products are marked with a special code consisting of 3 digits and a fourth control digit. The forth digit is determined by calculating the remainder of dividing the sum of the first three digits by 7. 
Define a function f(product_code) that returns True if the product code is correct or False otherwise. Sample result:"""

def f(product_code):
    if (int(product_code[0])+int(product_code[1])+int(product_code[2]))%7==int(product_code[3]):
        return True
    else:
        return False

if __name__ =="__main__":
    print(f("1114"))