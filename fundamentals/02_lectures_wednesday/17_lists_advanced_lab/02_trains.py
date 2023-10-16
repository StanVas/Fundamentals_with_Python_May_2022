number = int(input())
wagons = [0] * number

while True:
    command = input()

    if command == 'End':
        break

    data = command.split(' ')
    current_command = data[0]

    if current_command == 'add':
        people = int(data[1])
        wagons[-1] += people
    elif current_command == 'insert':
        index = int(data[1])
        people = int(data[2])
        wagons[index] += people
    elif current_command == 'leave':
        index = int(data[1])
        people = int(data[2])
        wagons[index] -= people

print(wagons)
