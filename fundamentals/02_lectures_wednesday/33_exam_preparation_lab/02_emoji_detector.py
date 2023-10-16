# https://judge.softuni.org/Contests/Practice/Index/2302#1
import re

text = input()
pattern = r'::[A-z][a-z]{2,}::|\*{2}[A-z][a-z]{2,}\*{2}'
emojis = re.findall(pattern, text)
cool_threshold = 1
digits = re.findall(r'\d', text)
for digit in digits:
    cool_threshold *= int(digit)
print(f'Cool threshold: {cool_threshold}')
print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for emoji in emojis:
    coolness = 0
    for ch in emoji:
        if ch != ':' and ch != '*':
            coolness += ord(ch)
    if coolness > cool_threshold:
        print(emoji)
