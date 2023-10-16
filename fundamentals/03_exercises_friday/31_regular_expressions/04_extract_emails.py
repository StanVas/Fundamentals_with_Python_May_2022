import re

string = input()
pattern = r'(?<=\s)(([a-z0-9]+[\_\-\.a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
result = re.findall(pattern, string)
for element in result:
    print(element[0])
