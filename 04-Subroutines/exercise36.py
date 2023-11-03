"""36.	A device in a door registers people entering and leaving a room. The + sign means a person entering a room and the – 
sign a person leaving a room. Define the function f(detector) that returns True if at least 3 people were in the room at the same time, or False otherwise. Sample result:"""
def f(detector):
    people=0
    result=False
    for x in detector:
        if x=="+":
            people+=1
        elif x=="-":
            people-=1
        if(people>=3):
            result=True
    return result

if __name__=="__main__":
    print(f("+-+++-+---"))