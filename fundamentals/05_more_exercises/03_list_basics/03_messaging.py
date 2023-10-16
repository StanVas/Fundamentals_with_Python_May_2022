number_lst = list(map(int, input().split()))
string = input()
# string_lst = string.split()
new_message = []


def split(word):
    return[char for char in word]


chr_lst = split(string)

for number in number_lst:
    digit_str = str(number)
    digit_map = map(int, digit_str)
    digit_lst = list(digit_map)
    num_sum = sum(digit_lst)
    if num_sum > len(chr_lst):
        num_sum -= len(chr_lst)
    # for index in range(len(chr_lst)):
    #     if index == num_sum:
    new_message.append(chr_lst[num_sum])
    chr_lst.pop(num_sum)
print(''.join(new_message))
