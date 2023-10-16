int_lst = list(map(int, input().split(', ')))
zero_count = int_lst.count(0)
zero_count = int(zero_count)

while 0 in int_lst:
    int_lst.remove(0)

for zero in range(zero_count):
    int_lst.append(0)

print(int_lst)
