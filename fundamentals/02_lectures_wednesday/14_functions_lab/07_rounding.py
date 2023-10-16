# print(list(map(lambda x: round(float(x)), input().split(' '))))


def round_nums(nums):
    result = [round(num) for num in nums]
    return result


numbers = list(map(float, input().split(' ')))
print(round_nums(numbers))
