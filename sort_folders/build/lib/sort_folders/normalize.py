import re

UKRAINIAN_SYMBOLS = 'абвгдеєжзиіїйклмнопрстуфхцчшщьюя'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "je", "zh", "z", "y", "i", "ji", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "ju", "ja")

TRANS = {}

for u, t in zip(UKRAINIAN_SYMBOLS, TRANSLATION):
    TRANS[ord(u)] = t
    TRANS[ord(u.upper())] = t.upper()

def normalize(name = str) -> str: 
    name, *extentions = name.split('.')
    new_name = name.translate(TRANS)
    new_name = re.sub(r'\W', '_', new_name)
    return f"{new_name}.{'.'.join(extentions)}"

    
if __name__ == '__main__':
    print(normalize('={H6йVЇQ.tar.gz'))