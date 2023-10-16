current_version = input().split('.')
s = [str(i) for i in current_version]
int_lst = str("".join(s))
next_version = int(int_lst) + 1
version = str(next_version)
last_version = []
for element in version:
    last_version += element

print(*last_version, sep='.')


#############
############# from the exersice
# version = [int(number) for number in input().split(".")]
# version[-1] += 1
# for current_index in range(len(version) - 1, -1, -1):
#     if version[current_index] > 9:
#         version[current_index] = 0
#         if current_index - 1 >= 0:
#             version[current_index - 1] += 1
# print('.'.join(str(number) for number in version))
