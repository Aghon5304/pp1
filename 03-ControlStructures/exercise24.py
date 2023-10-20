current_product_price = 140
previous_product_price= 200
if 100-(current_product_price/previous_product_price)*100 >=10:
    print("buy the product!!!")
    print(f"price reduced by {100-(current_product_price/previous_product_price )*100 }%")