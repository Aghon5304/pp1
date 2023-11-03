def f(binary_number):
    is_true=True
    for x in binary_number:
        if x !="0" and x!="1":
            is_true=False
    return is_true
print(f"f('101101') returns {f('101101')}")
f("1311a10100") 