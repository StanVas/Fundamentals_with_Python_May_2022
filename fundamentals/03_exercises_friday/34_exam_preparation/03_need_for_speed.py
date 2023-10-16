# https://judge.softuni.org/Contests/Practice/Index/2307#2

def cars_info(cars_dict, number):
    for _ in range(number):
        car = input().split('|')
        brand = car[0]
        mileage = car[1]
        fuel = car[2]

        cars_dict[brand] = {'mileage': int(mileage), 'fuel': int(fuel)}

    return cars_dict


def actions(cars_dict):
    while True:
        command = input()

        if command == 'Stop':
            break
        else:
            command = command.split(' : ')

        if command[0] == 'Drive':
            car = command[1]
            distance = int(command[2])
            fuel = int(command[3])
            if cars_dict[car]['fuel'] < fuel:
                print('Not enough fuel to make that ride')
            else:
                cars_dict[car]["fuel"] -= fuel
                cars_dict[car]['mileage'] += distance
                print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car]['mileage'] >= 100000:
                del_car = car
                del cars_dict[car]
                print(f"Time to sell the {del_car}!")

        elif command[0] == 'Refuel':
            car = command[1]
            fuel = int(command[2])
            if cars_dict[car]['fuel'] + fuel > 75:
                fuel = 75 - cars_dict[car]['fuel']
                cars_dict[car]['fuel'] = 75
            else:
                cars_dict[car]['fuel'] += fuel
            print(f"{car} refueled with {fuel} liters")

        elif command[0] == 'Revert':
            car = command[1]
            kilometers = int(command[2])
            if cars_dict[car]['mileage'] - kilometers < 10000:
                cars_dict[car]['mileage'] = 10000
            else:
                cars_dict[car]['mileage'] -= kilometers
                print(f"{car} mileage decreased by {kilometers} kilometers")

    return cars_dict


def additional_print(cars_dict):
    for element in cars_dict:
        fuel = cars_dict[element]['fuel']
        mileage = cars_dict[element]['mileage']
        print(f"{element} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


def need_for_speed(number):
    cars_dictionary = {}
    cars_info(cars_dictionary, number)
    actions(cars_dictionary)
    additional_print(cars_dictionary)


number_of_cars = int(input())
need_for_speed(number_of_cars)
