"""32.	Define the function f(n1,n2,n3), which returns True if at least one of the numbers n1,n2,n3 is negative or False otherwise. Sample result:"""
def f(n1,n2,n3):
    if n1<0 or n2<0 or n3<0:
        return True
    else:
        return False
    

if __name__=="__main__":
    print(f(11,6,-4))