class Instrument:
    
    def graj(self):
        raise NotImplementedError

class Strunowy(Instrument):
    
    def graj(self):
        return "Wydaje dzwiek w reakcji na szarpnięcie struny."
    
class Dety(Instrument):
    
class Gitara(Strunowy):
    
    def graj(self):
        return "Giatara w"+super().graj()[1:-1] + " palcem. "
    
class Skrzypce (Strunowy):
    
    def graj(self):
        return "Skrzypce "+super().graj()[1:-1].replace('Wydaje', 'wydaje', 1) + "smyczkiem. "
    
i = Instrument()
s = Strunowy()
g = Gitara()
s_ = Skrzypce()