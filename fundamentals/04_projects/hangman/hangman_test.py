# hangman - console game

import random

# Welcome screen and option to choose theme with words.

print('Игра - Бесеница -')
print()
print('Моля изберете тема: \n1. Спорт. \n2. Компютри. \n3. Дрехи. \n4. Музика. \n5. Професии.')
print()
theme = int(input('Тема: '))

# Main logic for the game.
# Randomly choose the word and print number of missing letters. Start guessing the word - letter by letter.
# Depend the length of the word there are exactly the same turns to guess it.

if theme == 1:

    # list with all words for the current theme

    list = ['баскетбол', 'волейбол', 'футбол', 'борба', 'плуване', 'колоездене', 'бадминтон']
    list_word = random.choice(list)
    guesses = ''
    turns = len(list_word)

    # loop for guessing the word

    while turns > 0:
        flag = 0

        # loop for printing the "_" char if it's empty or the correct letter if it's already guessed.

        for char in list_word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                flag += 1

        # loop when winning the game and guessed the correct word

        if flag == 0:
            print()
            print('Печелиш!')
            print(f'Думата е: {list_word}')
            break
        print()
        guess = input('Посочи буква: ')

        guesses += guess

        # Counting the mistakes that you made

        if guess not in list_word:
            turns -= 1
            print('Грешно')
            print(f'Остават ти {turns} опита!')

        if turns == 0:
            print('ГУБИШ')

if theme == 2:
    list = ['мишка', 'линукс', 'процесор', 'софтуер', 'клавиатура', 'фотошоп', 'захранване']
    list_word = random.choice(list)
    guesses = ''
    turns = len(list_word) + 3
    while turns > 0:
        flag = 0

        for char in list_word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                flag += 1

        if flag == 0:
            print()
            print('Печелиш!')
            print(f'Думата е: {list_word}')
            break
        print()
        guess = input('Посочи буква: ')

        guesses += guess

        if guess not in list_word:
            turns -= 1
            print('Грешно')
            print(f'Остават ти {turns} опита!')

        if turns == 0:
            print('ГУБИШ')

if theme == 3:
    list = ['рокля', 'колан', 'вратовръзка', 'панталон', 'пуловер', 'чорапогащник', 'костюм']
    list_word = random.choice(list)
    guesses = ''
    turns = len(list_word) + 3
    while turns > 0:
        flag = 0

        for char in list_word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                flag += 1

        if flag == 0:
            print()
            print('Печелиш!')
            print(f'Думата е: {list_word}')
            break
        print()
        guess = input('Посочи буква: ')

        guesses += guess

        if guess not in list_word:
            turns -= 1
            print('Грешно')
            print(f'Остават ти {turns} опита!')

        if turns == 0:
            print('ГУБИШ')

if theme == 4:
    list = ['композитор', 'музикант', 'цигулка', 'барабани', 'бийтмейкър', 'саксофон', 'кларинет']
    list_word = random.choice(list)
    guesses = ''
    turns = len(list_word) + 3
    while turns > 0:
        flag = 0

        for char in list_word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                flag += 1

        if flag == 0:
            print()
            print('Печелиш!')
            print(f'Думата е: {list_word}')
            break
        print()
        guess = input('Посочи буква: ')

        guesses += guess

        if guess not in list_word:
            turns -= 1
            print('Грешно')
            print(f'Остават ти {turns} опита!')

        if turns == 0:
            print('ГУБИШ')

if theme == 5:
    list = ['програмист', 'мениджър', 'заварчик', 'механизатор', 'моряк', 'финансист', 'земеделец']
    list_word = random.choice(list)
    guesses = ''
    turns = len(list_word) + 3
    while turns > 0:
        flag = 0

        for char in list_word:
            if char in guesses:
                print(char, end=' ')
            else:
                print('_', end=' ')
                flag += 1

        if flag == 0:
            print()
            print('Печелиш!')
            print(f'Думата е: {list_word}')
            break
        print()
        guess = input('Посочи буква: ')

        guesses += guess

        if guess not in list_word:
            turns -= 1
            print('Грешно')
            print(f'Остават ти {turns} опита!')

        if turns == 0:
            print('ГУБИШ')
