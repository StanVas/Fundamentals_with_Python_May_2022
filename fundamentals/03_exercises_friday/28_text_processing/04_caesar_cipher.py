text = input()
cipher_text = []
for ch in text:
    cipher_text.append(chr(ord(ch) + 3))
print(''.join(cipher_text))
