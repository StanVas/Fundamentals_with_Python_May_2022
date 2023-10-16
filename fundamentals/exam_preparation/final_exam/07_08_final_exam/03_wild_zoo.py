animals_dict = {}

while True:
    command = input()

    if command == 'EndDay':
        break
    else:
        command = command.split(': ')
        action = command[0]

        if action == 'Add':
            animal, needed_food, area = command[1].split("-")
            if animal not in animals_dict:
                animals_dict[animal] = {'needed_food': int(needed_food), 'area': area}
            else:
                animals_dict[animal]['needed_food'] += int(needed_food)

        elif action == 'Feed':
            animal, food = command[1].split('-')
            if animal in animals_dict:
                animals_dict[animal]['needed_food'] -= int(food)
                if animals_dict[animal]['needed_food'] <= 0:
                    del animals_dict[animal]
                    print(f"{animal} was successfully fed")

print('Animals:')
for animal in animals_dict:
    print(f" {animal} -> {animals_dict[animal]['needed_food']}g")

area_dict = {}
for animal in animals_dict:
    area = animals_dict[animal]['area']
    if area not in area_dict:
        area_dict[area] = {'count': 1}
    else:
        area_dict[area]['count'] += 1

print(f"Areas with hungry animals:")
for area in area_dict:
    print(f"{area}: {area_dict[area]['count']}")
