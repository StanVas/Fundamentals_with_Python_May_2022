def plants_info(number, plants_dict):
    for num in range(number):
        plant, rarity = input().split('<->')
        plants_dict[plant] = {'rarity': int(rarity), "rating": []}

    return plants_dict


def actions(plants_dict):
    while True:
        command = input().split(": ")
        action = command[0]
        if action == 'Exhibition':
            break
        else:
            data = command[1].split(' - ')
            plant = data[0]
            if plant not in plants_dict:
                print('error')
            else:
                if action == 'Rate':
                    rating = int(data[1])
                    plants_dict[plant]['rating'].append(rating)

                elif action == 'Update':
                    new_rarity = int(data[1])
                    plants_dict[plant]['rarity'] = new_rarity

                elif action == 'Reset':
                    plants_dict[plant]['rating'].clear()

    return plants_dict


def print_function(plants_dict):
    print("Plants for the exhibition:")
    for plant in plants_dict:
        average_rating = 0
        if len(plants_dict[plant]['rating']) > 0 and sum(plants_dict[plant]['rating']) > 0:
            average_rating = sum(plants_dict[plant]['rating']) / len(plants_dict[plant]['rating'])
        print(f'- {plant}; Rarity: {plants_dict[plant]["rarity"]}; Rating: {average_rating:.2f}')


number_of_plants = int(input())
plants_dict = {}
plants_info(number_of_plants, plants_dict)
actions(plants_dict)
print_function(plants_dict)
