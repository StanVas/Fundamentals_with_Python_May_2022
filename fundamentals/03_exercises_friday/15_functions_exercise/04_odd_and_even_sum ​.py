def list_int(num):
    list_int_num = []
    for element in num:
        list_int_num.append(int(element))
    return list_int_num


def odd_list_func():
    odd_list = []
    for element in list_int(number):
        if element % 2 != 0:
            odd_list.append(int(element))
    return odd_list


def even_list_func():
    even_list = []
    for element in list_int(number):
        if element % 2 == 0:
            even_list.append(int(element))
    return even_list


def odd_sum():
    odd = 0
    for current_num in odd_list_func():
        odd += current_num
    return odd


def even_sum():
    even = 0
    for current_num in even_list_func():
        even += current_num
    return even


number = input()
int_list = list_int(number)
int_odd_list = odd_list_func()
int_even_list = even_list_func()
int_odd_sum = odd_sum()
int_even_sum = even_sum()
print(f'Odd sum = {int_odd_sum}, Even sum = {int_even_sum}')
