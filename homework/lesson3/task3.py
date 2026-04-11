znaki = "Python jest super! "
zlaczony_tekst = "".join(znaki.split())



print(f"Zdanie z usuniętymi białymi znakami: {zlaczony_tekst}")
print(f"Zdanie jako ciąg małych liter: {znaki.lower()}")
print(znaki.replace("super","świetny"))
print(znaki[4])