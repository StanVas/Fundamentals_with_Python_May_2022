def sum_numbers(a, b):
    return a + b


def subtract_numbers(a, b):
    return a - b


def add_and_subtract(first, second, third):
    sum_first_second_int = sum_numbers(first, second)
    subtract_sum_third_int = subtract_numbers(sum_first_second_int, third)
    print(subtract_sum_third_int)


first_num = int(input())
second_num = int(input())
third_num = int(input())
add_and_subtract(first_num, second_num, third_num)
