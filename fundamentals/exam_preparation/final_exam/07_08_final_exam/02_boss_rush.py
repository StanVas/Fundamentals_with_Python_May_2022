import re

number_of_lines = int(input())
pattern = r'\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#'

for line in range(number_of_lines):
    info = input()
    result = re.findall(pattern, info)
    if not result:
        print("Access denied!")
    else:
        for element in result:
            print(f"{element[0]}, The {element[1]}")
            print(f'>> Strength: {len(element[0])}')
            print(f'>> Armor: {len(element[1])}')
