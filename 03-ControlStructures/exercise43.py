f_now=1
f_before=0
result=str(f_before)+", "+str(f_now)
for x in range(18):
    new_f=f_now+f_before
    result+=", "+str(new_f)
    f_before=f_now
    f_now=new_f
print(result)
