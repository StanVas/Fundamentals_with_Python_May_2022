def repeat_func(word):
    return word * len(word)


words: list = input().split(' ')
print(''.join(map(repeat_func, words)))
