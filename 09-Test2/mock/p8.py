import re
def f(arr):
    wynik=0
    for x in arr:
        if len(x)>=4 and len(x)<=12:
            a =len(re.findall("[a-z1-9_]+",x))
            if a==1:
                wynik+=1
    return wynik

if __name__=="__main__":
    print(f(["uek","water_7_x","anna.may","a_b_c_d_e_f"]))