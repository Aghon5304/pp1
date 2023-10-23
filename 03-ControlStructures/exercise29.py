jacket_time = 40
underwear_time = 70
shoes_time = 20
rinse_time = 15
spin_time = 9
final_time = 0
washing_product = "shoes" 
rinse = True
spin = False
if washing_product=="jacket":
    final_time+=jacket_time
    if rinse==True:
        final_time+=rinse_time
    if spin == True:
        final_time+=spin_time
else :
    if washing_product=="underwear":
        final_time+=underwear_time
        if rinse==True:
            final_time+=rinse_time
        if spin == True:
            final_time+=spin_time
    else :
        if washing_product=="shoes":
            final_time+=shoes_time
            if rinse==True:
                final_time+=rinse_time
            if spin == True:
                final_time+=spin_time
print(f"Total washing time: {final_time} minutes")
