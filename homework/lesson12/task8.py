
def dzialanie(a, b, znak):
    if znak == "+":
        return a + b
    elif znak == "-":
        return a - b
    elif znak == "/":
        return a/b
    elif znak == "*":
        return  a * b
    else:
        return("nie obsługiwnay znak ")
        
while True:
    try:
        tekst = input("Podaj pierwszą liczbę lub 'q' aby wyjść: ")
        
        if tekst == "q":
            break
        a = float(tekst)
        b = float(input("Podaj drugą liczbę: "))
        znak = input("Podaj znak (+, -, *, /): ")
        
        wynik = dzialanie(a, b, znak)
    
    except ValueError:
        print("Błąd: Podano nieprawidłową wartość. ")
    
    except ZeroDivisionError:
          print("Błąd: Nie można dzielić przez zero. ")
    
    else: 
          
          print("Wynik: ", wynik) 
          
    finally:
         print("Koniec obliczeń.\n")        