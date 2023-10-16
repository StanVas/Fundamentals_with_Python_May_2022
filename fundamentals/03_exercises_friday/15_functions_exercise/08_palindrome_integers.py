def palindrome_nums(nums):
    palindrome_lst = []
    for current_num in nums:
        if current_num == current_num[::-1]:
            palindrome_lst.append(True)
        else:
            palindrome_lst.append(False)
    return palindrome_lst


numbers = input().split(', ')
palindrome_list = palindrome_nums(numbers)
print(*palindrome_list, sep="\n")
# print('\n'.join([str(n == n[::-1]) for n in input().split(", ")])) # one line
