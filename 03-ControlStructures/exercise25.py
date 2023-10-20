number_of_products_bougth=int(input("number of products purchesed: "))
product_price = float(input("product price: "))
pay = 0
if (number_of_products_bougth>2):
    pay=2*product_price+product_price*(number_of_products_bougth-2)*(1-0.25)
else:
    pay=product_price
print(f"amount to pay: {pay}")