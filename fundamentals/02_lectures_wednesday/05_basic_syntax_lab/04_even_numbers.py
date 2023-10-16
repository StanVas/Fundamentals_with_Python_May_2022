lines = int(input())

for num in range(lines):
    number = int(input())
    current_num = number
    if current_num % 2 != 0:
        print(f'{current_num} is odd!')
        break
else:
    print('All numbers are even.')
