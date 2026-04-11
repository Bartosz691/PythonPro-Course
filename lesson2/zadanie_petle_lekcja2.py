#zapytaj kolejno użytkownika o imie, wiek i miasto W PĘTLI
#wypełnij danymi ze słownika zdanie
#A więc, masz na imię [imię], masz [Wiek]

#1. krok pętli: pytamy o imię i zapisuje do słownika
#2. krok pętli: pytamy o wiek i zapisuje do słownika
#3. krok pętlo: pytamy o miasto i zapisuje (do słownika)

def pobierz_uzytkownika()-> dict:
 dane_uzytkownika = {} # klucz : wartosc

 for informacja in ('imie', 'wiek', 'miasto'):
    dane_uzytkownika[informacja] = input("wprowadz "+informacja+": ")
    
 return dane_uzytkownika

#pytamy użytkownika o ilość użytkowników do wprowadzenia
# w pętli pytamy o kolejnych użytkowników
# słowniki są przechowywane w liscie

#stworzenie pustej listy
#pobrac ilosc uzytkowników
#pętla for iterujemy po range

users = []
liczba_uzytkownik = int(input('Podaj liczbę użytkowników: '))
if liczba_uzytkownik <=0:
    print('liczba użytkowników musi być większa od 0')
else:
    #liczba użytkowników = 3
    
    #while liczba_uzytkownik != 0:
    #    user = pobierz_uzytkownika()
    #    users.append(user)
    #    liczba_uzytkownik= liczba_uzytkownik-1
        
 #while len(users) < 3:
 #    user = pobierz_uzytkownika()
 #    users.append(user)         
 
 for _ in range(liczba_uzytkownik): #gdy i w pętli for niw jest potrzebne to dajemy podłogę
     user = pobierz_uzytkownika()
     users.append (user)
     
     