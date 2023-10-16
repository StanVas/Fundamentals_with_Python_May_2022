characters = int(input())
total_sum = 0

for char in range(characters):
    current_chr = input()
    total_sum += ord(current_chr)

print(f'The sum equals: {total_sum}')
