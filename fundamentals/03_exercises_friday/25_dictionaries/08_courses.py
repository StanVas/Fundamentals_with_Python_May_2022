courses = {}
command = input()

while ':' in command:
    course, student = command.split(' : ')
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course].append(student)
    command = input()

for key in courses:
    length_dict = {key: len(value) for key, value in courses.items()}
    length_key = length_dict[key]
    print(f'{key}: {length_key}')
    for element in courses[key]:
        print(f'-- {element}')
