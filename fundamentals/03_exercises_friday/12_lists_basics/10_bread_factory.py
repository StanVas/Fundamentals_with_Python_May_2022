list_of_events = input().split('|')
energy = 100
coins = 100
bakery_is_open = True
for event in list_of_events:
    event_info = event.split('-')
    type_of_event = event_info[0]
    number = int(event_info[1])
    if type_of_event == 'rest':
        temporary_energy = energy
        energy += number
        if energy > 100:
            energy = 100
        gained_energy = energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif type_of_event == 'order':
        if energy >= 30:
            energy -= 30
            coins += number
            print(f'You earned {number} coins.')
        else:
            energy += 50
            print('You had to rest!')
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            bakery_is_open = False
            break
if bakery_is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
