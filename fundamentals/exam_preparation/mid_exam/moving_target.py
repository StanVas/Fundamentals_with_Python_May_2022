def shoot_target(index, power, targets):
    if 0 <= index < len(targets):
        if targets[index] - power <= 0:
            targets.pop(index)
        else:
            targets[index] -= power
    return targets


def add_target(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print('Invalid placement!')
    return targets


def strike_target(index, radius, targets):
    index_validator = index - radius >= 0 and index + radius < len(targets)
    if index_validator:
        starting_index = index - radius
        final_index = index + radius
        targets = [targets[i] for i in range(len(targets)) if i < starting_index or i > final_index]
    else:
        print('Strike missed!')
    return targets


def moving_targets(targets):
    while True:
        command = input()
        if command == 'End':
            print('|'.join([str(num) for num in targets]))
            break

        command = command.split(' ')
        action = command[0]
        index = int(command[1])
        value = int(command[2])

        if action == 'Shoot':
            targets = shoot_target(index, value, targets)
        elif action == 'Add':
            targets = add_target(index, value, targets)
        elif action == 'Strike':
            targets = strike_target(index, value, targets)


data = list(map(int, input().split(' ')))
moving_targets(data)
