names = input().split(', ')


result = sorted(names, key=lambda item: (-len(item), item))   # -len sorting from biggest to smallest
# result = sorted(names, key=lambda item: (len(item), item))  # without - is sorting from smallest to biggest
# result = sorted(names, key=lambda x: (-len(x), x))

print(result)
