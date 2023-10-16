import re

string = input()
pattern = r'([#@])([A-Za-z]{3,})\1{2}([A-Za-z]{3,})\1'
result = re.findall(pattern, string)
mirror_words = []
if len(result) == 0:
    print("No word pairs found!")
else:
    print(f'{len(result)} word pairs found!')

for element in result:
    first_word = element[1]
    second_word = element[2]
    second_word_check = element[2][::-1]
    if first_word == second_word_check:
        mirror_words.append(f'{first_word} <=> {second_word}')

if len(mirror_words) == 0:
    print("No mirror words!")
else:
    print("The mirror words are:")
    print(', '.join(mirror_words))
