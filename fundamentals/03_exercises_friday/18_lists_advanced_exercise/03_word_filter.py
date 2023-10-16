string_lst = input().split(' ')
final_lst = []
for element in string_lst:
    if len(element) % 2 == 0:
        final_lst.append(element)

print('\n'.join(final_lst))
