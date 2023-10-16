students = {}
number_of_students = int(input())

for _ in range(number_of_students):
    student = input()
    grade = float(input())
    if student not in students:
        students[student] = []
    students[student].append(grade)

for key in students:
    sum_dict = {key: sum(value) for key, value in students.items()}
    sum_key = sum_dict[key]
    length_dict = {key: len(value) for key, value in students.items()}
    length_key = length_dict[key]
    result = sum_key / length_key
    if result >= 4.5:
        print(f'{key} -> {result:.2f}')
