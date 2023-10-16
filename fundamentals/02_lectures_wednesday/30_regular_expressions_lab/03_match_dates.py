import re

dates = input()
date_pattern = r"(\d{2})([/\.-])([A-Z][a-z]{2})\2(\d{4})"
result = re.findall(date_pattern, dates)
for element in result:
    print(f'Day: {element[0]}, Month: {element[2]}, Year: {element[3]}')
