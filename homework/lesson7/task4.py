import math

def czy_pierwsza(n)->bool:
    if n < 2:
        return False
    else: 
     for i in range(2, int(math.sqrt(n)) + 1):
       if n % i == 0:
          return False
    return True

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

liczby_pierwsze = list(filter(czy_pierwsza, liczby))

print(liczby_pierwsze)
