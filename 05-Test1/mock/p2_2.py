'''
(p2.py) Define the function f(n1,n2,n3) that returns True if all three numbers n1,n2,n3
 are different or False otherwise. Sample result:
f(4,8,5) returns True
f(2,9,2) returns False
'''
def f(n1,n2,n3):
    if n1!=n2 and n2!=n3 and n1!=n3:
        return True
    else: 
        return False
if __name__=='__main__':
    print(f(4,8,5))
    print(f(2,9,2))