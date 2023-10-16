first_string = input().split(', ')
second_string = input().split(', ')
final_string = []
for word_first in first_string:
    for word_second in second_string:
        if word_first in word_second:
            final_string.append(word_first)
            break
print(final_string)
