import re

numbers = input()
number_pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
result = re.finditer(number_pattern, numbers)

for match in result:
    print(match.group(), end=' ')


# Check print by print!
# import re
# numbers = input()
# number_pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
# result = re.compile(number_pattern)
# matches = list(result.finditer(numbers))
# print(matches)
# for element in matches:
#     print(element.group())
#     print(element)
