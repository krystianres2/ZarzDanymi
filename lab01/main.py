# C:\Users\kryst\OneDrive\Pulpit\Python\lab1\Scripts\activate
import json
from difflib import get_close_matches
data = json.load(
    open('data.json', encoding="UTF-8")
)
# print(type(data))

# zad1
# print(f'Data from simple JSON\n{data}')

headers = list(data.keys())

def translate(ui):
    if ui in headers:
        return data[ui]
    elif ui.capitalize() in headers:
        return data[ui.capitalize()]
    elif ui.upper() in headers:
        return data[ui.upper()]
    elif len(get_close_matches(ui, headers)) > 0:
        closestWord = get_close_matches(ui, headers)
        res = input(f'Czy chciałeś podać {closestWord}? Podaj T lub N: ')
        if res == 'T':
            return data[closestWord[0]]
        elif res == 'N':
            return f'Wyraz = {ui} nie istnieje w pliku. Sprawdź ponownie.'
        else:
            return "Nieprawidłowa litera"
        
# def getCloseMatches(word, data):
#     ratios = []
#     for i in data:
#         ratios.append(SequenceMatcher(None, word, i).ratio())
#     return data[ratios.index(max(ratios))]
# def getCloseMatches(word, data):
#     return get_close_matches(word, possibilities, n=3, cutoff=0.6)


user_input = input('Podaj wyraz: ').lower()
output = translate(user_input)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)

# print(f'{translate(user_input)}')

