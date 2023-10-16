first_chr = input()
second_chr = input()


def ascii_result(first, second):
    collected_ascii = []
    for current_chr in range(ord(first) + 1, ord(second)):
        collected_ascii.append(chr(current_chr))
    return collected_ascii


result = ascii_result(first_chr, second_chr)
print(' '.join(result))
# print(*result, sep=" ")
