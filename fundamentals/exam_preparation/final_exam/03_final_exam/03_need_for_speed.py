def obtain_cars(number, car_dict):
    for car in range(number):
        car = input().split("|")
        brand = car[0]
        mileage = int(car[1])
        fuel = int(car[2])
        car_dict[brand] = {'mileage': mileage, 'fuel': fuel}

    return car_dict


def actions(cars_dict):
    while True:
        command = input()
        if command == 'Stop':
            break
        else:
            command = command.split(' : ')
            action = command[0]
            if action == 'Drive':
                car = command[1]
                distance = int(command[2])
                fuel = int(command[3])
                if fuel > cars_dict[car]['fuel']:
                    print('Not enough fuel to make that ride')
                else:
                    cars_dict[car]["mileage"] += distance
                    cars_dict[car]['fuel'] -= fuel
                    print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
                    if cars_dict[car]['mileage'] >= 100000:
                        del cars_dict[car]
                        print(f"Time to sell the {car}!")

            elif action == 'Refuel':
                car = command[1]
                fuel = int(command[2])
                if cars_dict[car]['fuel'] + fuel > 75:
                    difference = 75 - cars_dict[car]['fuel']
                    cars_dict[car]['fuel'] += difference
                    print(f"{car} refueled with {difference} liters")
                else:
                    cars_dict[car]['fuel'] += fuel
                    print(f"{car} refueled with {fuel} liters")

            elif action == 'Revert':
                car = command[1]
                kilometers = int(command[2])
                cars_dict[car]['mileage'] -= kilometers
                if cars_dict[car]['mileage'] < 10000:
                    cars_dict[car]['mileage'] = 10000
                else:
                    print(f"{car} mileage decreased by {kilometers} kilometers")
    return cars_dict


def print_func(cars_dict):
    for car in cars_dict:
        mileage = cars_dict[car]['mileage']
        fuel = cars_dict[car]['fuel']
        print(f"{car} -> Mileage: {mileage} kms, Fuel in the tank: {fuel} lt.")


def need_for_speed(number):
    cars_dict = {}
    obtain_cars(number, cars_dict)
    actions(cars_dict)
    print_func(cars_dict)


number_of_cars = int(input())
need_for_speed(number_of_cars)
