number = input()


def max_number(num):
    return int(''.join(sorted(str(num), reverse=True)))


print(max_number(number))
