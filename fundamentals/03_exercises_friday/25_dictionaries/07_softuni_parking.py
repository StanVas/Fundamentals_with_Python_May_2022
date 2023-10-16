parking_users = {}
number_of_commands = int(input())

for command in range(number_of_commands):
    current_command = input().split()
    action = current_command[0]
    if action == 'register':
        user_name = current_command[1]
        number_plate = current_command[2]
        if user_name in parking_users.keys():
            print(f"ERROR: already registered with plate number {number_plate}")
        else:
            parking_users[user_name] = number_plate
            print(f"{user_name} registered {number_plate} successfully")
    elif action == 'unregister':
        user_name = current_command[1]
        if user_name not in parking_users:
            print(f"ERROR: user {user_name} not found")
        else:
            print(f"{user_name} unregistered successfully")
            del parking_users[user_name]
for key in parking_users:
    print(f'{key} => {parking_users[key]}')
