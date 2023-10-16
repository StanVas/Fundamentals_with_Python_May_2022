# import math
#
# points = tuple(math.floor(float(input())) for _ in range(4))
# sum_x = sum([abs(num) for num in points[:2]])
# sum_y = sum([abs(num) for num in points[2:]])
#
#
# def whats_closer(arg1, arg2):
#     if arg1 <= arg2:
#         return points[:2]
#     return points[2:]
#
#
# print(whats_closer(sum_x, sum_y))
# print(sum_x, sum_y)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())


def center_point(num1, num2, num3, num4):
    result1 = abs(num1) + abs(num2)
    result2 = abs(num3) + abs(num4)
    if result1 == result2:
        return f'({int(num1)}, {int(num2)})'
    elif result1 > result2:
        return f'({int(num3)}, {int(num4)})'
    else:
        return f'({int(num1)}, {int(num2)})'


print(center_point(x1, y1, x2, y2))
