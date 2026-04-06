tall = int(input("Podaj wzrost dziecka: "))
czyopiekun = input("czy dziecko wchodzi z opiekunem? ")

if czyopiekun == 'tak':
    value = True
elif czyopiekun == 'nie':
    value = False
    
moze_wejsc = tall >= 120 and value or tall >= 160
print(f"czy może wejść: {moze_wejsc}")