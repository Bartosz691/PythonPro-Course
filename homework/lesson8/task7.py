dict_ = {"a": 1,
         'b': 2}

def pobierz_wartosc(dict_: dict, key):
    return dict_.get(key)

def pobierz_wartosc_wtry(dict_: dict, key):
    try:
         return dict_[key] # KeyError
    except KeyError:
        return None
def pobierz_wartosc_if(dict_: dict, key):
    try:
        return dict_[key] #KeyError
    except KeyError:
        return None
    
wzrost_uczniow = {'ania': 170,
                  'piotrek': 179}