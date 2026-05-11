class Figura:
  def oblicz_pole():
     pass
 
class Kwadrat(Figura):
    def __init__(self, bok):
       super().__init__(bok)
       return self.oblicz_pole(bok * bok)
   
class Kolo(Figura):
    def __init__(self, promien):
       super().__init__(promien)
       PI = 3.14159
       return self.oblicz_pole(PI * (promien * promien))
   
figura1 = Kwadrat(6)
figura2 = Kolo(4)

lista_figur = [figura1, figura2]

print("Pola figur: ")
for pole in lista_figur:
    print(pole)