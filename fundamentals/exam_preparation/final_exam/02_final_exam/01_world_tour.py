destinations = input()

while True:
    command = input()
    if command == 'Travel':
        print(f"Ready for world tour! Planned stops: {destinations}")
        break
    else:
        command = command.split(":")
        if command[0] == 'Add Stop':
            index = int(command[1])
            string = command[2]
            if 0 <= index < len(destinations):
                destinations = destinations[:index] + string + destinations[index:]
            print(destinations)
        elif command[0] == 'Remove Stop':
            start_index = int(command[1])
            end_index = int(command[2])
            if 0 <= start_index <= end_index < len(destinations):
                destinations = destinations[:start_index] + destinations[end_index + 1:]
            print(destinations)
        elif command[0] == 'Switch':
            old_str = command[1]
            new_str = command[2]
            if old_str in destinations:
                destinations = destinations.replace(old_str, new_str)
            print(destinations)
