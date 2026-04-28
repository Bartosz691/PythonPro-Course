class WiekNiepoprawnyError(Exception):
    
 def rejestruj_uzytkownika(wiek):
       if wiek < 18:
          raise WiekNiepoprawnyError(f"Wiek jest za niski")
       print("rejestracja przebiegła pomyślnie")
 try:
      rejestruj_uzytkownika(15)
 except WiekNiepoprawnyError as e:
     print("jestes niepełnoletni, kod błędu: ", e.args[1])