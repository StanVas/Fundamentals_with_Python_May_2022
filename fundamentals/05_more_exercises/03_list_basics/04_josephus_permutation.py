def remove_numbs(step, int_lst):
    final_lst = []
    position = step - 1
    idx = 0
    len_list = (len(int_lst))
    while len_list > 0:
        idx = (position + idx) % len_list
        final_lst.append(int_lst[idx])
        int_lst.pop(idx)
        len_list -= 1
    return final_lst


num_list = list(map(int, input().split()))
step_k = int(input())
final = remove_numbs(step_k, num_list)
print(str(final).replace(" ", ""))
