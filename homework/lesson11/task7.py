class Telewizor:
    ZAKRES_GLOSNOSCI = (0, 100)
    
    def __init__(self) -> None:
        self.__kanal = 1
        self.__glosnosc = 10
        self.__wlaczony = False
        
    def glosniej(self, wartosc: int):
        print('Podgłaśniamy o wartosc', wartosc)
        self.__zmien_glosnosc(wartosc)
        
    def ciszej(self, wartosc: int):
        print('Sciszamy o wartosc', wartosc)
        self.__zmien_glosnosc(-wartosc)
        
    def on_off(self):
        self.__wlaczony = not self.__wlaczony
        
    def wlacz(self):
        self.__wlaczony = True
    
    def wylacz(self):
        self.__wlaczony = True  
        
    def ustaw_kanal(self, nowy_kanal):
        if not self.__wlaczony:
            raise ValueError("Telewizor musi być włączony, aby zmienić kanał.")
        self.__kanal = nowy_kanal
    
    def info(self):
        print(f'[{"ON" if self.__wlaczony else "OFF"}][{self.__glosnosc=}][{self.__kanal=}]')    
        
    def __zmien_glosnosc(self, wartosc: int):
        if not isinstance(wartosc, int):
            raise TypeError
        print('zmieniono glosnosc o', wartosc)
        self.__glosnosc += wartosc
        
t = Telewizor()
