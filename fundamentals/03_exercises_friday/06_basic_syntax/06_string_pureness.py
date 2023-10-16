strings_numb = int(input())

for string in range(strings_numb):
    current_word = input()
    if ',' in current_word or '.' in current_word or '_' in current_word:
        print(f'{current_word} is not pure!')
    else:
        print(f'{current_word} is pure.')
