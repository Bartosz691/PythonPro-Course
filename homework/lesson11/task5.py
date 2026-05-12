from math import pi

class Figura:
  def oblicz_pole(self):
     pass
 
class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok
        
    def oblicz_pole(self):
       return self.bok ** 2


class Kolo(Figura):
    PI = 3.14159
    
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return self.PI * self.promien ** 2
    
    #@property
    #def promien(self):
    #    return self.oblicz_pole()
   
figura1 = Kwadrat(6)
figura2 = Kolo(4)

lista_figur = [figura1, figura2]

print("Pola figur: ")
for fig in lista_figur:
    print(fig.oblicz_pole())