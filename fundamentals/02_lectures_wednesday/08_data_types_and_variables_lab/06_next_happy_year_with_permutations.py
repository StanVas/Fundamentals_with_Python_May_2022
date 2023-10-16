from itertools import permutations

number = tuple(map(int, input()))
mypermutation = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], len(number))

for digits in list(mypermutation):
    if digits > number:
        result = ''.join(str(x) for x in digits)
        print(result)
        break

# syntax: new_list = [expression for item in iterable if condition == True]
# The return value is a new list, leaving the old list unchanged.
# example:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# new_list = [x for x in fruits if "a" in x]
# print(new_list)
# example:
# new_list = [x for x in fruits if x != "apple"]
# new_list = [x for x in range(10)]
# new_list = [x for x in range(10) if x < 5]
# new_list = [x.upper() for x in fruits]
# new_list = ['hello' for x in fruits]
# new_list = [x if x != "banana" else "orange" for x in fruits]
