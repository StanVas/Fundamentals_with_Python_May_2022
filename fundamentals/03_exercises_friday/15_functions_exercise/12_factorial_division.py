def first_factorial(num):
    first_result = 1
    for current_num in range(1, num + 1):
        first_result *= current_num
    return first_result


def second_factorial(num):
    second_result = 1
    for current_num in range(1, num + 1):
        second_result *= current_num
    return second_result


first_number = int(input())
second_number = int(input())
result = first_factorial(first_number) / second_factorial(second_number)
print(f'{result:.2f}')
