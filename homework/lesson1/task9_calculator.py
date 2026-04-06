liczba1 = float(input("Podaj pierwszą liczbę: "))

liczba2 = float(input("Podaj drugą liczbę: "))

znak = input("Podaj znak operacji: ")

if znak == '+':
    result = liczba1 + liczba2
elif znak == '-':
     result = liczba1 - liczba2
elif znak == '*':
     result = liczba1 * liczba2
elif znak == '/':
     result = liczba1 / liczba2
     
print(f"wynik działania wynosi: {result}")