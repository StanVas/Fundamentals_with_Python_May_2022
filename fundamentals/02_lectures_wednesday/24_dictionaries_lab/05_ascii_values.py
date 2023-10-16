ascii_lst = input().split(', ')
code_lst = []
ascii_dict = {}

for ch in ascii_lst:
    code = ord(ch)
    if code in code_lst:
        continue
    else:
        code_lst.append(code)

# ascii_dict = {ascii_lst[x]: code_lst[y] for x in range(len(ascii_lst)), y in range(len(code_lst))}

list(zip(ascii_lst, code_lst))
for (x, y) in zip(ascii_lst, code_lst):
    ascii_dict[x] = y

print(ascii_dict)
