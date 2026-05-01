from pathlib import Path
sciezka_do_pliku = Path("D:\PythonPro-Course\homework\lesson9\dziennik.txt")
    
with open(sciezka_do_pliku, 'a', encoding='utf-8') as f:
    while True:
     linia = input("Podaj nową linię: ")
     
     if linia == 'koniec':
         break
     
     f.write(linia + "\n")