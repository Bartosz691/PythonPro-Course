slowo = input("podaj slowo: ")

dlugosc_slowo = len(slowo)
for idx in range(dlugosc_slowo):
    print(idx, slowo[idx])
    
for idx, znak in enumerate(slowo):
    print(idx, znak)