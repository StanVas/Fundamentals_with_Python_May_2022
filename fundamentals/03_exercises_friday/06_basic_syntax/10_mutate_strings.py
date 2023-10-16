first_string = input()
second_string = input()
last_string = first_string
for symbol_index in range(len(second_string)):
    left_part = second_string[:symbol_index + 1]
    right_part = first_string[symbol_index + 1:]
    current_sting = left_part + right_part
    if current_sting == last_string:
        continue
    print(current_sting)
    last_string = current_sting
