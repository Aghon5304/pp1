price = float(input("Enter price:"))
discount =int(input("Enter discount in %")) 
reduction= price*discount/100
print(f"Price with discount: {'%.2f' % (price-reduction)}\nReduction: {'%.2f' %reduction}")