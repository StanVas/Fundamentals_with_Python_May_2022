# list unpack
# lst = ['a', 'b', 'c', 'd']
# num_lst = [1, 2, 3, 4]
# print(*num_lst, sep='\n')   # on new line
# print(*num_lst)         # same line
# print(*lst, sep='\n')   # the same - works with numbers and str
# print('\n'.join(lst))   # the same - works only with str
# print(*palindrome_list, sep="\n")
# print('\n'.join([str(n == n[::-1]) for n in input().split(", ")])) # one line
#
#
# input  - convert to int
# list(map(int, input().split()))
# lst = [int(x) for x in input().split(" ")]
#
# current_element = [i for i, x in enumerate(targets) if x == element] # finds index=see mid_exam=shoot_for_the_win
# return from int list to str list
# return ''.join([str(num) for num in numbers])
#
# print(sum([num ** 2 for num in range(1000)]))
#
#
# print([num for num in range(5)])
# print(list(range(5)))
#
#
# nums = [1, 2, 3, 4, 5, 6]
# evens = [num for num in nums if num % 2 == 0]
# print(evens)
# filtered = [True if x % 2 == 0 else False for x in nums]
# print(filtered)
# result = [num for num in nums if num % 2 == 0 if num > 2 if num != 6]
# print(result)
#
#
# matrix = [[x for x in range(3)] for y in range(3)]
# print(matrix)
#
#
# lst = [1, 2, 3, 4, 5, 6, 7, 8]
# lst += [4]
# lst.append(4)   # only one element
# lst.extend([4, 5])  # multiple elements
# lst.insert(1, 4)  # insert index - element
# lst.pop() or lst.pop(3) # removes by index
# lst.remove(1)  # removes by element(only the first found)
# lst[1] = -1  # replace in lst index with given value
# del lst[1,5]  # deletes from index 1 to index 5
# print(lst)
#
#
# lst = [1, 2, 3, 4]
# print(list(filter(lambda x: x % 2 == 0, lst)))
# print([num for num in lst if num % 2 == 0])
#
#
# lst = [1, 2, 3, 4, 6, 7, 2, 2, 2]
# print(lst.count(2))
# print(lst.index(2))  # finds first index that has this element
# lst.reverse()  # reverse permanent
# print(lst)
# print(lst[::-1])  # not permanent
# print('\n'.join([str(n == n[::-1]) for n in input().split(",")]))  # reverse
#
#
# lst = [6, 2, 3, 1, 5, 7, 8]
# sorted = not permanent
# sort = permanent
# def even_nums(num):
#     return num % 2
#
#
# sorted_lst = sorted(lst)
# sorted_nums = sorted(lst, key=even_nums)
# print(sorted(lst, reverse=True))   # reverse
# print(sorted(lst, key=lambda x: - x))  # reverse
# print(sorted_lst)   # sort
# print(sorted_nums)   # sort with function, still keep the rest
#
#
#
#        MAP
# print(list(map(lambda x: x * 2, [1, 2, 3, 4, 5, 6])))
#
#
# def square_numbers(n):
#     return n ** 2
# print(list(map(square_numbers, [1, 2, 3, 4, 5, 6])))
#
#
# lst_num = [1, 2, 3, 4, 5, 6]
# print(list(map(square_numbers, lst_num)))
#
#
# map - str to int
# string_lst = ['1', '2', '3', '4']
# number_lst = list(map(int, string_lst))
# print(number_lst)
#
# lst_num = [1, 2, 3, 4, 5, 6]
# even_nums = list(filter(lambda x: x % 2 == 0, lst_num))
# print(even_nums)
#
#
# Swap
# nums = [1, 2, 3]
# nums[0], nums[1], nums[2] = nums[2], nums[1], nums[0]
# print(nums)
#
#
# nums_1 = [1, 2, 3]
# nums_2 = [4, 5, 6]
# final_list = nums_1 + nums_2
# print(final_list)
# print(nums_1 + nums_2)
#
#
# SET   =  returns unique list but in a random arrangement
# nums = [1, 2, 3, 2, 4, 6, 3, 2, 3, 2, 3]
# unique_nums = list(set(nums))
# print(unique_nums)
#
#
#
# number = '3456'   # sum with string
# sum = int(number[0]) + int(number[3])
# print(sum)
