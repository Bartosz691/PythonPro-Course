class Punkt:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f'x: "{self.x}" , y: "{self.y}'
    
punkt  = Punkt(125,65)

print(punkt)