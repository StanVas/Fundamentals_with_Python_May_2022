import random
guess_counter = 0
questions = ['2 * 2 = ?', 'Largest country by size?', 'Largest country by population?']
answered_questions = []
for _ in range(4):
    current_question = random.choice(questions)
    if current_question not in answered_questions:
        answered_questions.append(current_question)
        print(current_question)
    else:
        continue
    if current_question == '2 * 2 = ?':
        answer = input('your answer: ')
        if answer == '4':
            print('right answer\n')
            guess_counter += 1
        else:
            print('wrong answer')
    elif current_question == 'Largest country by size?':
        answer = input('your answer: ')
        if answer == 'Russia':
            print('right answer\n')
            guess_counter += 1
        else:
            print('wrong answer')
    elif current_question == 'Largest country by population?':
        answer = input('your answer: ')
        if answer == 'China':
            print('right answer\n')
            guess_counter += 1
        else:
            print('wrong answer')

