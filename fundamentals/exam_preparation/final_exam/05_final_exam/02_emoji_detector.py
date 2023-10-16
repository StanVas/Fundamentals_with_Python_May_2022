import re

text = input()
pattern = r'([*]{2})([A-Z][a-z]{2,})\1|([:]{2})([A-Z][a-z]{2,})(:{2})'
match = re.finditer(pattern, text)
some_lst = []
cool_threshold = re.findall(r'\d', text)
cool_threshold_total = 1
for number in cool_threshold:
    cool_threshold_total *= int(number)
print(f'Cool threshold: {cool_threshold_total}')
for group in match:
    some_lst.append(group.group())
print(f'{len(some_lst)} emojis found in the text. The cool ones are:')
for element in some_lst:
    score = 0
    for ch in element:
        if ch.isalpha():
            score += ord(ch)
    if score >= cool_threshold_total:
        print(element)
