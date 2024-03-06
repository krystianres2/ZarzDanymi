import json
data = json.load(
    open('simple_data.json', encoding="UTF-8")
)

# print(type(data))

# zad1
# print(f'Data from simple JSON\n{data}')

# zad2

headers = list(data.keys())
print(headers)

def nasza_funkcja(ui):
    if ui in data.keys():
        return data[ui]
    else:
        return f'Podanego słowa {ui} nie ma w słowniku'

user_input = input('Podaj wyraz: ').lower()
print(f'Result: \n{nasza_funkcja(user_input)}')

# getCloseMatches