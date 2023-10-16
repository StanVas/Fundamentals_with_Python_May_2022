number = '12345678'
for index, digit in enumerate(number):
    print(index, digit)
# показва индекс и после какво се намира на него(по този начин принтираме и двете)



# обхождане на обратно
some_string = 'Goshoepich'
new_string = ''
# for char in range(len(some_string) - 1, -1, -1):
#     new_string += some_string[char]
# print(new_string)
print(some_string[::-1])
# (start : end : step)     ---
# range(start, end, step)  --- двете изглеждат еднакви
print(some_string[::1])
print(some_string[:1])
print(some_string[3::3])
print(some_string[:5:3]) #   end : step
print(some_string[:5:])  # end:
# a[-1]    # last item in the array
# a[-2:]   # last two items in the array
# a[:-2]   # everything except the last two items
# a[::-1]    # all items in the array, reversed
# a[1::-1]   # the first two items, reversed
# a[:-3:-1]  # the last two items, reversed
# a[-3::-1]  # everything except the last two items, reversed