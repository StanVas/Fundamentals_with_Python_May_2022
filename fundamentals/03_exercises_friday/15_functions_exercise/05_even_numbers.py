# numbers_as_digits = [int(s) for s in input().split()]
# numbers_as_digits = [int(s) for s in input().split() if int(s)%2==0]
numbers_as_string = input().split()
numbers_as_digits = []
for current_num in numbers_as_string:
    numbers_as_digits.append(int(current_num))
is_even = lambda x: x % 2 == 0
result = list(filter(is_even, numbers_as_digits))
print(result)



# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False
#
#
# numbers = input().split()
# filtered_numbers = []
# for current_number in numbers:
#     filtered_numbers.append(int(current_number))
# print(filtered_numbers)