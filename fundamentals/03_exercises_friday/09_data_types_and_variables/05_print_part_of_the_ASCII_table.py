first_character = int(input())
last_character = int(input())

for character in range(first_character, last_character + 1):
    print(chr(character), end=" ")
