temps = [12,15,14,18,20,19,24,21,18,17,24]

def desc_temp(dane):
    if dane>=20:
        return 'warm'
    elif dane<=10:
        return 'cold'
    else:
        return 'med_warm'
    
for i in temps:
    print(desc_temp(i))