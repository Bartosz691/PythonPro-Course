import json

logs_path = r"D:\PythonPro-Course\homework\lesson9\logs.csv"
keyword = input("Podaj słowo klucz do wyszukania w logach: ")

def write_keylog(line: str, keylog_filepath: str | Path = "keylogs.csv"):
    if not line.endswith('\n'):
        line+='\n'
    with open(keylog_filepath, 'w', encoding='utf8') as klfp:
        klfp.write(line)
        
    with open(keylog_filepath, 'r', encoding='utf-8') as klfp:
        klfp.write(line)
        
with open(logs_path, 'r', encoding='utf-8') as lfp:
    for line in lfp:
        
        if keyword in line:
            write_keylog(line)