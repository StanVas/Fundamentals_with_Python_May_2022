def position(alphabet):
    return format(ord(alphabet) - 96)


text = input().split()
total_sum = 0
for element in text:
    number = int(element[1:-1])
    new_number = 0
    first_letter = element[0]
    last_letter = element[-1]
    position_first = int(position(first_letter.lower()))
    position_last = int(position(last_letter.lower()))
    if first_letter.isupper():
        new_number = number / position_first
    elif first_letter.islower():
        new_number = number * position_first
    if last_letter.isupper():
        new_number -= position_last
    elif last_letter.islower():
        new_number += position_last
    total_sum += new_number

print(f'{total_sum:.2f}')
