text = input()
lst = []
for letter in text:
    lst.append(letter)


def capital_indexes(word):
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []
    for index, ch in enumerate(word):
        if ch in upper:
            result.append(index)
    return result


print(capital_indexes(text))
