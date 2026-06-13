# Zasób na serwerze:
# {
#     "name": "Katarzyna",
#     "email": "k.nowak@example.com",
#     "city": "Warszawa"
# }

# PUT - wysyłamy cały zasób po zmianie

put_body = {
    "name": "Kasia",
    "email": "k.nowak@example.com",
    "city": "Warszawa"
}

# PATCH - wysyłamy tylko zmienione pole

patch_body = {
    "name": "Kasia"
}

print("PUT:")
print(put_body)

print("\nPATCH:")
print(patch_body)

# PUT zastępuje cały zasób, dlatego trzeba wysłać wszystkie pola.
# PATCH aktualizuje tylko wskazane pola.
# PATCH jest bardziej oszczędny pod względem ilości przesyłanych danych.