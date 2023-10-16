# https://judge.softuni.org/Contests/Practice/Index/2518#2


def greate_plants_data(plants, number):
    for _ in range(number):
        data = input().split('<->')
        name_of_plant = data[0]
        rarity = int(data[1])
        if name_of_plant not in plants:
            plants[name_of_plant] = {'rarity': rarity, 'rating': []}
        else:
            plants[name_of_plant]['rarity'] = rarity
    return plants


def additional_plants_data(plants):
    while True:
        command = input().split(': ')
        current_command = command[0]
        if current_command == 'Exhibition':
            break
        else:
            data = command[1].split(' - ')
            current_plant = data[0]
            if current_plant not in plants:
                print('error')
                continue
            if current_command == 'Rate':
                rating = int(data[1])
                plants[current_plant]['rating'].append(rating)
            elif current_command == 'Update':
                rarity = int(data[1])
                plants[current_plant]['rarity'] = rarity
            elif current_command == 'Reset':
                plants[current_plant]["rating"].clear()
    return plants


def print_function(plants):
    print("Plants for the exhibition:")
    for dict_element in plants:
        if len(plants[dict_element]['rating']) > 0 and sum(plants[dict_element]['rating']) > 0:
            average_rating = sum(plants[dict_element]['rating']) / len(plants[dict_element]['rating'])
        else:
            average_rating = 0
        rarity = plants[dict_element]['rarity']
        print(f"- {dict_element}; Rarity: {rarity}; Rating: {average_rating:.2f}")


def plan_discovery(number):
    plants = {}

    greate_plants_data(plants, number)
    additional_plants_data(plants)
    print_function(plants)


n = int(input())
plan_discovery(n)
