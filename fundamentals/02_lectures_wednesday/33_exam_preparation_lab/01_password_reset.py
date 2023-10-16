# judge => https://judge.softuni.org/Contests/Practice/Index/2303#0

def password_reset():
    password = input()
    while True:
        command = input().split()
        current_command = command[0]
        if current_command == 'Done':
            print(f'Your password is: {password}')
            break
        elif current_command == 'TakeOdd':
            password = ''.join([password[i] for i in range(len(password)) if i % 2 != 0])
            print(password)
        elif current_command == 'Cut':
            index = int(command[1])
            length = int(command[2])
            password = ''.join([password[i] for i in range(len(password)) if i < index or i >= index + length])
            print(password)
        elif current_command == 'Substitute':
            substring = command[1]
            substitute = command[2]
            if substring not in password:
                print('Nothing to replace!')
            else:
                password = password.replace(substring, substitute)
                print(password)


password_reset()
