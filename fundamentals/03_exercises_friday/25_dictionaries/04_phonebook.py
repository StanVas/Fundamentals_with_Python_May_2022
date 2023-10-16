phonebook = {}

while True:
    command = input()
    if '-' not in command:
        break

    name, number = command.split('-')
    phonebook[name] = number
for check_contact in range(int(command)):
    current_contact = input()
    if current_contact in phonebook.keys():
        print(f'{current_contact} -> {phonebook[current_contact]}')
    else:
        print(f'Contact {current_contact} does not exist.')
