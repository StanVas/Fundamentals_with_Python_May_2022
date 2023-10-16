import re

password = input()

while True:
    command = input()
    if command == 'Complete':
        break
    else:
        command = command.split()
        action = command[0]
        if action == 'Make':
            case = command[1]
            index = int(command[2])
            if case == 'Upper':
                password = password[:index] + password[index].upper() + password[index + 1:]
                print(password)
            elif case == 'Lower':
                password = password[:index] + password[index].lower() + password[index + 1:]
                print(password)

        elif action == 'Insert':
            index = int(command[1])
            char = command[2]
            if 0 <= index <= len(password):
                password = password[:index] + char + password[index:]
                print(password)

        elif action == 'Replace':
            char = command[1]
            value = command[2]
            if char in password:
                char_value = ord(char) + int(value)
                password = password.replace(char, chr(char_value))
                print(password)

        elif action == 'Validation':
            if len(password) < 8:
                print("Password must be at least 8 characters long!")
            pattern = r"^[A-Za-z0-9_]*$"
            result = re.search(pattern, password)
            if not result:
                print("Password must consist only of letters, digits and _!")
            digits = ''
            lower_case = ''
            upper_case = ''
            for ch in password:
                if ch.isdigit():
                    digits += ch
                if ch.isupper():
                    upper_case += ch
                if ch.islower():
                    lower_case += ch
            if len(upper_case) == 0:
                print("Password must consist at least one uppercase letter!")
            if len(lower_case) == 0:
                print("Password must consist at least one lowercase letter!")
            if len(digits) == 0:
                print("Password must consist at least one digit!")
