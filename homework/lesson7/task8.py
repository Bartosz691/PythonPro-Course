liczby = [-5, 2, 8, -1, 0, 10]

dodatnieikwadraty = list(map(lambda x: x * x, filter(lambda x: x >= 0, liczby)))

print(dodatnieikwadraty)