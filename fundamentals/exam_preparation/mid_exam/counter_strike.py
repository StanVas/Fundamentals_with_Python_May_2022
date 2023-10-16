energy = int(input())
battle_counter = 0

while True:
    command = input()
    if battle_counter % 3 == 0:
        energy += battle_counter
    if command == 'End of battle':
        print(f'Won battles: {battle_counter}. Energy left: {energy}')
        break
    else:
        if energy >= 0 and energy - int(command) >= 0:
            energy -= int(command)
            battle_counter += 1
            continue
        else:
            print(f'Not enough energy! Game ends with {battle_counter} won battles and {energy} energy')
            break
