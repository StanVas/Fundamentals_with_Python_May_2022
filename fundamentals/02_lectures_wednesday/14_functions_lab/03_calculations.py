def calculations(a, b, operator):
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = int(a / b)
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return result


type_of_operation = input()
first_num = int(input())
second_num = int(input())

print(calculations(first_num, second_num, type_of_operation))
