# https://judge.softuni.org/Contests/Practice/Index/2303#2
def heroes_info(heroes_dict, number):
    for _ in range(number):
        hero, hp, mp = input().split()
        heroes_dict[hero] = {'hp': int(hp), 'mp': int(mp)}

    return heroes_dict


def play_the_game(heroes_dict):
    while True:
        command = input()
        if command == 'End':
            break
        else:
            command = command.split(' - ')
        if command[0] == 'CastSpell':
            hero = command[1]
            mp_needed = int(command[2])
            spell = command[3]
            if heroes_dict[hero]["mp"] < mp_needed:
                print(f"{hero} does not have enough MP to cast {spell}!")
            else:
                heroes_dict[hero]["mp"] -= mp_needed
                print(f"{hero} has successfully cast {spell} and now has {heroes_dict[hero]['mp']} MP!")

        elif command[0] == 'TakeDamage':
            hero = command[1]
            damage = int(command[2])
            attacker = command[3]
            heroes_dict[hero]['hp'] -= damage
            current_hp = heroes_dict[hero]['hp']
            if heroes_dict[hero]['hp'] > 0:
                print(f"{hero} was hit for {damage} HP by {attacker} and now has {current_hp} HP left!")
            else:
                del_hero = hero
                del heroes_dict[hero]
                print(f"{del_hero} has been killed by {attacker}!")

        elif command[0] == 'Recharge':
            hero = command[1]
            amount_mana = int(command[2])
            if heroes_dict[hero]['mp'] + amount_mana > 200:
                amount_mana = 200 - heroes_dict[hero]['mp']
                heroes_dict[hero]['mp'] = 200
            else:
                heroes_dict[hero]['mp'] += amount_mana
            print(f"{hero} recharged for {amount_mana} MP!")
        elif command[0] == 'Heal':
            hero = command[1]
            amount_health = int(command[2])
            if heroes_dict[hero]['hp'] + amount_health > 100:
                amount_health = 100 - heroes_dict[hero]['hp']
                heroes_dict[hero]['hp'] = 100
            else:
                heroes_dict[hero]['hp'] += amount_health
            print(f"{hero} healed for {amount_health} HP!")

    return heroes_dict


def additional_print(heroes_dict):
    for element in heroes_dict:
        hp = heroes_dict[element]['hp']
        mp = heroes_dict[element]['mp']
        print(element)
        print(f'  HP: {hp}')
        print(f'  MP: {mp}')


def heroes_of_code_and_logic(number):
    heroes_dict = {}
    heroes_info(heroes_dict, number)
    play_the_game(heroes_dict)
    additional_print(heroes_dict)


number_of_heroes = int(input())
heroes_of_code_and_logic(number_of_heroes)
