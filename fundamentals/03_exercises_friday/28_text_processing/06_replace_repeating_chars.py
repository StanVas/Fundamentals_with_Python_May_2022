text = input()
new_text = ['test']
for char in text:
    if char == new_text[-1]:
        continue
    else:
        new_text.append(char)

print(''.join(new_text[1::]))
