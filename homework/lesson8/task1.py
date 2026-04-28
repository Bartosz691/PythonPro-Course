while True:
    try:
         fnum = input("Podaj pierwszą liczbę: ")
         snum = input("Podaj drugą liczbę: ")
         dzialanie  = input("podaj działanie [+,-,/,*]")  
         func_dict = {"+":  lambda x, y: x+y, 
                      "-":lambda x, y: x-y,
                      "*": lambda x, y: x*y,
                      "/": lambda x, y: x/y
                      }  
         func_dict[dzialanie](fnum, sum)
    except ValueError as e:
        err = e
        print("Podano niepoprawną liczbę")
    except KeyError:
        print("niepoprawne działanie ")
    except ZeroDivisionError:
        print("Druga liczba nie może wynosić 0 w przypadku dzielenia.")
    finally:
        print("runda kolejna")
    break