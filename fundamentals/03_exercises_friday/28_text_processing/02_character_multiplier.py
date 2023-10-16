first_string, second_string = input().split()
result = 0
difference = abs(len(first_string) - len(second_string))
if len(first_string) > len(second_string):
    for index in range(len(second_string)):
        result += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(first_string) - difference, len(first_string)):
        result += ord(first_string[index])
elif len(first_string) < len(second_string):
    for index in range(len(first_string)):
        result += ord(first_string[index]) * ord(second_string[index])
    for index in range(len(second_string) - difference, len(second_string)):
        result += ord(second_string[index])
elif len(first_string) == len(second_string):
    for index in range(len(first_string)):
        result += ord(first_string[index]) * ord(second_string[index])

print(result)
