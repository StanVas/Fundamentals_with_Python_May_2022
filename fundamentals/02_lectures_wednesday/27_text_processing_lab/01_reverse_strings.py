def reverse(data):
    for string in data:
        print(f'{string} = {string[::-1]}')


words = []
while True:
    command = input()
    if command == 'end':
        break
    words.append(command)

reverse(words)
