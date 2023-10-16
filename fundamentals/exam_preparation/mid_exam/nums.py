# def lst_of_five(some_lst):
#     some_lst = [i for i, v in enumerate(some_lst) if i < 5]
#     return some_lst
#

numbers_lst = list(map(int, input().split()))

average = sum(numbers_lst) / len(numbers_lst)

greater_than_average = [n for n in numbers_lst if n > average]
greater_than_average.sort(reverse=True)

if not greater_than_average:
    print('No')
if len(greater_than_average) <= 5:
    print(*greater_than_average)
# if len(greater_than_average) > 5:
#     print([n for n in range(len(greater_than_average), 0, 5)])
elif len(greater_than_average) > 5:
    print(*greater_than_average[0:5])
