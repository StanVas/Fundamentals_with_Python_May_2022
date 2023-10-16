import operator


def calculations(number_a, number_b, operation):
    operation_dict = {'multiply': operator.mul, 'divide': operator.truediv,
                      'add': operator.add, 'subtract': operator.sub}

    return int(operation_dict[operation](number_a, number_b))


type_of_operation = input()
first_num = int(input())
second_num = int(input())
print(calculations(first_num, second_num, type_of_operation))
