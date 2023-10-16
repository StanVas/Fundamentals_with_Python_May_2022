def repeat_func(word):
    return word * len(word)


words: list = input().split(' ')
print(''.join(map(repeat_func, words)))
#
# # the same one
# print(''.join(map(lambda word: word * len(word), input().split(' '))))


# examples for input: text ; abc text; Hi Softuni

# string methods in python documentation
