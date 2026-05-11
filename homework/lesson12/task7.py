#klasa Data z atrybutami: rok, miesiac, dzien
#napisać metodę ze stringa, która przyjmuje format 'DD-MM-RRRR'

class Data:
    
    def __init__(self, rok, mies, dzien):
        self.rok :int = rok
        self.mies: int = mies
        self.dzien: int = dzien
    
    @classmethod
    def ze_str(cls, data_str: str):
        "Data_str format= 'DD-MM-RRRR' "
        mapped_to_ints = map(int, data_str.split("-"))
        print(list(mapped_to_ints)[::-1])
        #cls()
        
data = Data(1909, 3, 10)
Data.ze_str("19-03-2023")