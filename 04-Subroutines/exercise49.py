'''49.	The sequence of digits contains the number of points rolled with a dice. Define a function f(dice) that returns a number specifying the number of dice rolled the most times in a row. Sample result:'''

def f(dice):
    max=0
    result=""
    for x in dice:
        count=0
        for y in dice:
            if x==y:
                count+=1
            else:
                if count>max:
                    result=x
                    max = count
                count=0
        if count>max:
           result=x
           max = count
    return result
                
if __name__ =="__main__":
    print(f('111144444111'))
    print(f("2133")) 
    print(f('5233165554211'))