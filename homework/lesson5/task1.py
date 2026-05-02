wiek = int(input("Podaj wiek: "))

if wiek >= 0 and wiek < 1:
    print("Niemowle")
elif wiek >= 2 or wiek <= 12:
    print("Dziecko")
elif wiek >= 13 and wiek <= 17:
    print("Nastolatek")
elif wiek >= 18 and wiek <= 64:
    print("Dorosły")
else:
    print("Senior")