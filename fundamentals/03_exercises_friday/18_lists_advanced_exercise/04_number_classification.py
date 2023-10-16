numbers_int = [int(number) for number in input().split(', ')]


def positive_numbers(numbers):
    return [number for number in numbers if number >= 0]


def negative_numbers(numbers):
    return [number for number in numbers if number < 0]


def even_numbers(numbers):
    return [number for number in numbers if number % 2 == 0]


def odd_numbers(numbers):
    return [number for number in numbers if number % 2 != 0]


print(f"Positive:", end=" ")
print(*(positive_numbers(numbers_int)), sep=', ')
print(f"Negative:", end=" ")
print(*negative_numbers(numbers_int), sep=', ')
print(f"Even:", end=" ")
print(*even_numbers(numbers_int), sep=', ')
print(f"Odd:", end=" ")
print(*odd_numbers(numbers_int), sep=', ')
