def oblicz_srednia(*args):
    if len(args) == 0:
        return 0

    return sum(args) / len(args)


print(oblicz_srednia(5, 4, 3, 5, 4))
print(oblicz_srednia(6, 6, 5))
print(oblicz_srednia())
