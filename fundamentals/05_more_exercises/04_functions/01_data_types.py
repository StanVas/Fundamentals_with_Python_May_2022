def read_input(something):
    if something == 'int':
        number = int(input())
        result = number * 2
        return result
    elif something == 'real':
        number = float(input())
        result = number * 1.5
        return f'{result:.2f}'
    elif something == 'string':
        string = input()
        return f'${string}$'


first_input = input()
print(read_input(first_input))
