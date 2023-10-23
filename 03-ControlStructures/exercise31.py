x = int(input("x = "))
y = int(input("y = "))
if x>=0:
    if y>0:
        print(f"Point P({x},{y}) is in the first quadrant of the coordinate system")
    else:  
        print(f"Point P({x},{y}) is in the second quadrant of the coordinate system")
else:
    if y>0:
        print(f"Point P({x},{y}) is in the third quadrant of the coordinate system")
    else:  
        print(f"Point P({x},{y}) is in the fourth quadrant of the coordinate system")
