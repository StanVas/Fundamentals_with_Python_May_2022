# https://judge.softuni.org/Contests/Practice/Index/2302#0

key = input()
while True:
    command = input().split(">>>")
    action = command[0]
    if action == 'Generate':
        print(f"Your activation key is: {key}")
        break
    if action == 'Contains':
        substring = command[1]
        if substring in key:
            print(f'{key} contains {substring}')
        elif substring not in key:
            print('Substring not found!')
    elif action == 'Flip':
        case = command[1]
        start_index = int(command[2])
        end_index = int(command[3])
        if case == 'Upper':
            key = key[:start_index] + key[start_index:end_index].upper() + key[end_index:]
            print(key)
        else:
            key = key[:start_index] + key[start_index:end_index].lower() + key[end_index:]
            print(key)
    elif action == "Slice":
        start_index = int(command[1])
        end_index = int(command[2])
        key = key[:start_index] + key[end_index:]
        print(key)
