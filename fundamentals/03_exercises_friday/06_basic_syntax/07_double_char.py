command = input()

while command != 'End':
    new_string = ''
    for char in range(len(command)):
        new_string += command[char] * 2
    if command == "SoftUni":
        command = input()
        continue
    print(new_string)
    command = input()
    if command == 'End':
        break
