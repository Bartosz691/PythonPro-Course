
def pobierz_uzytkownika()-> dict:
 dane_uzytkownika = {} # klucz : wartosc

 for informacja in ('imie', 'wiek', 'miasto'):
    dane_uzytkownika[informacja] = input("wprowadz "+informacja+": ")
    
 return dane_uzytkownika



def pobierz_n_uzytkownikow(ilosc_uzytkownikow):
    users = []
    for _ in range(ilosc_uzytkownikow):
        user = pobierz_uzytkownika()
        users.append(user)
       
    
    return users

liczba_uzytkownikow = int(input('podaj liczbe uzytkownikow: '))
if liczba_uzytkownikow <=0:
    print('liczba musi byc wieksza od 0')
else:
    users = pobierz_n_uzytkownikow(liczba_uzytkownikow)


