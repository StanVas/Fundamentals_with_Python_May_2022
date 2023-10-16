########### doesn't work ##########
#
# numbers_lst = [int(number) for number in input().split(', ')]
#
# if max(numbers_lst) % 10 == 0:
#     number_of_groups = max(numbers_lst) // 10
# else:
#     number_of_groups = max(numbers_lst) // 10 + 1
#
# for current_group in range(number_of_groups):
#     group_lst = [[num for num in numbers_lst if num // 10 == current_group]]
#
#     current_group = (current_group + 1) * 10
#
#     print(f"Group of {current_group}'s:", end=" ")
#     print(*group_lst)
#

######  solution colegue ############

numbers = list(map(int, input().split(", ")))
copy_numbers = numbers.copy()
group = 10

while len(numbers) > 0:
    tens = []
    for num in numbers:
        if num <= group:
            tens.append(num)
    print(f"Group of {group}'s: {tens}")
    for copy_num in tens:
        if copy_num in numbers:
            numbers.remove(copy_num)
    group += 10


# # it's a rather ugly solution, but it works fine, so I'm not touching it
#
# from math import ceil
#
# numbers = [int(num) for num in input().split(", ") if int(num) >= 0]
# groups = []
#
# # construct list with empty groups based on the highest number
# # it's necessary to round up with ceil
# for num in range(ceil(max(numbers) / 10)):
#     groups.append([])
#
# # check each number and append to the proper group
# for index, number in enumerate(numbers):
#     for i in range(1, len(groups) + 1):
#         if number <= i * 10:  # using indices as if they're 10, 20, 30 etc.
#             groups[i - 1].append(number)
#             break
#
# for index, group in enumerate(groups):
#     print(f"Group of {index + 1}0's: {group}")
