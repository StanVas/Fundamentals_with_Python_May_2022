def result_factorial(num):
    for factorial in range(1, num):
        num *= factorial
    return num


first_number = int(input())
second_number = int(input())

first_number_factorial = result_factorial(first_number)
second_number_factorial = result_factorial(second_number)
result = first_number_factorial / second_number_factorial
print(f'{result:.2f}')
