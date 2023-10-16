numbers = int(input())
positive_list = []
negative_list = []
for i in range(numbers):
    current_number = int(input())
    if current_number >= 0:
        positive_list += [current_number]
    else:
        negative_list += [current_number]

print(positive_list)
print(negative_list)
print(f'Count of positives: {len(positive_list)}')
print(f'Sum of negatives: {sum(negative_list)}')
