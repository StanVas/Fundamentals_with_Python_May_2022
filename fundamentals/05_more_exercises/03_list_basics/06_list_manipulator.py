def exchange(some_list, some_index):
    lst_len = len(some_list)
    if some_index < 0 or some_index > lst_len:
        print('Invalid index')
    else:
        split_lst = lst_len - some_index
        first_old_lst = some_list[:split_lst]
        second_old_lst = some_list[split_lst:]
        new_lst = second_old_lst + first_old_lst
        print(new_lst)


def max_even_odd(some_list, command):
    even_lst = []
    odd_lst = []
    result = 0
    if command == 'even':
        for num in some_list:
            if num % 2 == 0:
                even_lst.append(num)
        if len(even_lst) == 0:
            print('No matches')
        else:
            result = max(even_lst)
            index = some_list.index(result)
            return index

    if command == 'odd':
        for num in some_list:
            if num % 2 != 0:
                odd_lst.append(num)
        if len(odd_lst) == 0:
            print('No matches')
        else:
            result = max(odd_lst)
            index = some_list.index(result)
            print(index)


def min_even_odd(some_list, command):
    even_lst = []
    odd_lst = []
    result = 0
    if command == 'even':
        for num in some_list:
            if num % 2 == 0:
                even_lst.append(num)
        if len(even_lst) == 0:
            print('No matches')
            exit()
        else:
            result = min(even_lst)
            index = some_list.index(result)
            print(index)

    if command == 'odd':
        for num in some_list:
            if num % 2 != 0:
                odd_lst.append(num)
        if len(odd_lst) == 0:
            print('No matches')
        else:
            result = min(odd_lst)
            index = some_list.index(result)
            print(index)


def first_even_odd(some_list, some_count, command):
    even_lst = []
    odd_lst = []
    if command == 'even':
        for num in some_list:
            if num % 2 == 0:
                even_lst.append(num)
        if some_count > len(some_list):
            print("Invalid count")
        if some_count > len(even_lst):
            print(even_lst)
        else:
            first_even = even_lst[0:{some_count}]
            print(first_even)
    if command == 'odd':
        for num in some_list:
            if num % 2 != 0:
                odd_lst.append(num)
        if some_count > len(some_list):
            print("Invalid count")
        if some_count > len(odd_lst):
            print(odd_lst)
        else:
            first_odd = odd_lst[0:{some_count}]
            print(first_odd)


def last_even_odd(some_list, some_count, command):
    even_lst = []
    odd_lst = []
    if command == 'even':
        for num in some_list:
            if num % 2 == 0:
                even_lst.append(num)
        if some_count > len(some_list):
            print("Invalid count")
        if some_count > len(even_lst):
            print(even_lst)
        else:
            even_lst.reverse()
            first_even = even_lst[0:{some_count}]
            print(first_even)
    if command == 'odd':
        for num in some_list:
            if num % 2 != 0:
                odd_lst.append(num)
        if some_count > len(some_list):
            print("Invalid count")
        if some_count > len(odd_lst):
            print(odd_lst)
        else:
            odd_lst.reverse()
            first_odd = odd_lst[0:{some_count}]
            print(first_odd)


number_lst = list(map(int, input().split(" ")))
action_n = input()
while action_n != 'end':
    if action_n == 'end':
        break
    action = action_n.split()
    current_command = action[0]
    if current_command == 'exchange':
        index = int(action[1])
        exchange(number_lst, index)
    elif current_command == 'max':
        even_odd = action[1]
        print(max_even_odd(number_lst, even_odd))
    elif current_command == 'min':
        even_odd = action[1]
        min_even_odd(number_lst, even_odd)
    elif current_command == 'first':
        current_count = int(action[1])
        even_odd = action[2]
        first_even_odd(number_lst, current_count, even_odd)
    elif current_command == 'last':
        current_count = int(action[1])
        even_odd = action[2]
        last_even_odd(number_lst, current_count, even_odd)
    action_n = input()