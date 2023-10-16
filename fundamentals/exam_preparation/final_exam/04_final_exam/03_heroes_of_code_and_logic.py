def greate_party(number, some_dict):
    for num in range(number):
        string = input().split()
        hero = string[0]
        health = int(string[1])
        mana = int(string[2])
        some_dict[hero] = {'health': health, 'mana': mana}

    return some_dict


def play_the_game(some_dict):
    while True:
        command = input()
        if command == 'End':
            break
        else:
            command = command.split(' - ')
            action = command[0]

            if action == 'CastSpell':
                hero = command[1]
                mp_needed = int(command[2])
                spell_name = command[3]
                if some_dict[hero]['mana'] >= mp_needed:
                    some_dict[hero]['mana'] -= mp_needed
                    print(f"{hero} has successfully cast {spell_name} and now has {some_dict[hero]['mana']} MP!")
                else:
                    print(f"{hero} does not have enough MP to cast {spell_name}!")

            elif action == 'TakeDamage':
                hero = command[1]
                dmg = int(command[2])
                attacker = command[3]
                some_dict[hero]['health'] -= dmg
                if some_dict[hero]['health'] <= 0:
                    del some_dict[hero]
                    print(f"{hero} has been killed by {attacker}!")
                else:
                    print(f"{hero} was hit for {dmg} HP by {attacker} and now has {some_dict[hero]['health']} HP left!")

            elif action == 'Recharge':
                hero = command[1]
                amount_mana = int(command[2])
                some_dict[hero]['mana'] += amount_mana
                if some_dict[hero]['mana'] > 200:
                    difference = 200 - (some_dict[hero]['mana'] - amount_mana)
                    some_dict[hero]['mana'] = 200
                    print(f"{hero} recharged for {difference} MP!")
                else:
                    print(f"{hero} recharged for {amount_mana} MP!")

            elif action == 'Heal':
                hero = command[1]
                amount_health = int(command[2])
                some_dict[hero]['health'] += amount_health
                if some_dict[hero]['health'] > 100:
                    difference = 100 - (some_dict[hero]['health'] - amount_health)
                    some_dict[hero]['health'] = 100
                    print(f"{hero} healed for {difference} HP!")
                else:
                    print(f"{hero} healed for {amount_health} HP!")

    return some_dict


def print_func(some_dict):
    for hero in some_dict:
        print(hero)
        print(f'  HP: {some_dict[hero]["health"]}')
        print(f'  MP: {some_dict[hero]["mana"]}')


number_of_heroes = int(input())
heroes_dict = {}
greate_party(number_of_heroes, heroes_dict)
play_the_game(heroes_dict)
print_func(heroes_dict)
