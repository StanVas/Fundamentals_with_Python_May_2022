def receiving_cities(some_dict):
    while True:
        command = input()
        if command == 'Sail':
            break
        else:
            city, population, gold = command.split('||')
            if city in some_dict:
                some_dict[city]['population'] += int(population)
                some_dict[city]['gold'] += int(gold)
            else:
                some_dict[city] = {'population': int(population), 'gold': int(gold)}

    return some_dict


def sail(some_dict):
    while True:
        command = input()
        if command == 'End':
            break
        else:
            command = command.split('=>')

        if command[0] == 'Plunder':
            town = command[1]
            people = int(command[2])
            gold = int(command[3])
            some_dict[town]['population'] -= people
            some_dict[town]['gold'] -= gold
            print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
            if some_dict[town]['population'] <= 0 or some_dict[town]['gold'] <= 0:
                del some_dict[town]
                print(f"{town} has been wiped off the map!")

        elif command[0] == 'Prosper':
            town = command[1]
            gold = int(command[2])
            if gold < 0:
                print("Gold added cannot be a negative number!")
            else:
                some_dict[town]['gold'] += gold
                print(f"{gold} gold added to the city treasury. {town} now has {some_dict[town]['gold']} gold.")

    return some_dict


def print_func(some_dict):
    if len(some_dict) > 0:
        print(f'Ahoy, Captain! There are {len(some_dict)} wealthy settlements to go to:')
        for city in some_dict:
            population = some_dict[city]['population']
            gold = some_dict[city]['gold']
            print(f'{city} -> Population: {population} citizens, Gold: {gold} kg')
    else:
        print("Ahoy, Captain! All targets have been plundered and destroyed!")


def anno():
    cities_dict = {}
    receiving_cities(cities_dict)
    sail(cities_dict)
    print_func(cities_dict)


anno()
