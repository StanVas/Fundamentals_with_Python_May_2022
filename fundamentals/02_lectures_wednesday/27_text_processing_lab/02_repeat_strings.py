string = input().split(" ")
final_lst = []
for element in string:
    final_element = element * len(element)
    final_lst.append(final_element)

print("".join(final_lst))

# Mario
# result = [word * len(word) for word in string]
# print(''.join(result))

# Lambda
# print(''.join(map(lambda word: word * len(word), input().split(' '))))

# Function
# def repeat_func(word):
#     return word * len(word)
#
#
# words: list = input().split(' ')
# print(''.join(map(repeat_func, words))
