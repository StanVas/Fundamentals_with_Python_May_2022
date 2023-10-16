command = ''
while command != 'Welcome!':
    command = input()
    if command == 'Welcome!':
        continue
    if command == 'Voldemort':
        print("You must not speak of that name!")
        break
    else:
        for char in range(len(command)):
            if len(command) < 5:
                print(f'{command} goes to Gryffindor.')
                break
            elif len(command) == 5:
                print(f'{command} goes to Slytherin.')
                break
            elif len(command) == 6:
                print(f'{command} goes to Ravenclaw.')
                break
            elif len(command) > 6:
                print(f'{command} goes to Hufflepuff.')
                break
if command == 'Welcome!':
    print("Welcome to Hogwarts.")
