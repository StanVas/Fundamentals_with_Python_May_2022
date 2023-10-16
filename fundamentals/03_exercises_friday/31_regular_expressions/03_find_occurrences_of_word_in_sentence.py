import re

string = input()     # .lower() this is done on line 7
key_word = input()

pattern = fr'\b({key_word})\b'
result = re.findall(pattern, string, flags=re.IGNORECASE)
print(len(result))
