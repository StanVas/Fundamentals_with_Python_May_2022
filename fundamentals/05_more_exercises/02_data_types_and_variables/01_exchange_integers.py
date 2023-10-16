first_num = int(input())
second_num = int(input())
lst_num = [first_num, second_num]


def exchange(lst):
    second_lst = lst[0], lst[1] = lst[1], lst[0]
    return second_lst


print('Before:')
print(f'a = {lst_num[0]}')
print(f'b = {lst_num[1]}')
exchange(lst_num)
print('After:')
print(f'a = {lst_num[0]}')
print(f'b = {lst_num[1]}')
