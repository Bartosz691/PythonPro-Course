czy_student = input("Czy jest studentem? ")
wiek = int(input("Podaj wiek: "))

status_znizki = "Przyznano 50%" if czy_student == 'tak' or wiek < 18 else "Cena 100zl"

print(status_znizki)