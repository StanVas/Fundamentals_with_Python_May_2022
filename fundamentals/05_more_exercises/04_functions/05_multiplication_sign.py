first_num = int(input())
second_num = int(input())
third_num = int(input())


def positive_or_negative(num1, num2, num3):
    if num1 == 0 or num2 == 0 or num3 == 0:
        return 'positive'
    elif num1 < 0 and num2 < 0 and num3 < 0:
        return 'negative'
    elif num1 < 0 and num2 < 0 or num1 < 0 and num3 < 0 or num2 < 0 and num3 < 0:
        return 'positive'
    elif num1 < 0 or num2 < 0 or num3 < 0:
        return 'negative'
    else:
        return 'positive'


print(positive_or_negative(first_num, second_num, third_num))
