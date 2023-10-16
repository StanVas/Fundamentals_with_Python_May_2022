password = input()

while True:
    command = input()

    if command == 'Done':
        print(f'Your password is: {password}')
        break

    else:
        command = command.split(' ')
        action = command[0]
        if action == 'TakeOdd':
            password = ''.join([password[i] for i in range(len(password)) if i % 2 != 0])
            print(password)

        elif action == 'Cut':
            index = int(command[1])
            length = int(command[2])
            password = password[:index] + password[index + length:]
            print(password)

        elif action == 'Substitute':
            substring = command[1]
            substitute = command[2]
            if substring in password:
                password = password.replace(substring, substitute)
                print(password)
            else:
                print("Nothing to replace!")
