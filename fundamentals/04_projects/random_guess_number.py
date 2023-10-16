import random

number = random.randint(1, 3)

guess_number = int(input('Enter number between 1 and 3: '))
if guess_number == number:
    print('Success')
