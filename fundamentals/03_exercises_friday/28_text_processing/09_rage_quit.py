# string = input().upper()
# new_string = ''
# unique_ch = ''
# text = ''
# digits = ''
# for ch in string:
#     if len(digits) > 0 and ch.isdigit():
#         digits += ch
#         new_string += text * int(digits)
#         text = ''
#         digits = ''
#     if not ch.isdigit() and len(digits) > 0:
#         new_string += text * int(digits)
#         text = ''
#         digits = ''
#     if ch.isdigit() and len(digits) == 0:
#         digits += ch
#
#     if not ch.isdigit():
#         text += ch
#         if ch not in unique_ch:
#             unique_ch += ch
#
#
# print(f'Unique symbols used: {len(unique_ch)}')
# print(new_string)

# string = input().upper()
# new_string = ''
# unique_ch = ''
# text = ''
# digits = ''
# for ch in string:
#     if not ch.isdigit():
#         text += ch
#         if ch not in unique_ch:
#             unique_ch += ch
#     elif ch.isdigit():
#         digits += ch
#         for index in range(len(string)):
#             if ch[index] == len(string):
#                 new_string += text * int(digits)
#                 text = ''
#                 digits = ''
#             else:
#                 next_number = ch[index+1]
#                 if next_number.isdigit():
#                     print(next_number)
#         else:
#             new_string += text * int(digits)
#             text = ''
#             digits = ''
# print(f'Unique symbols used: {len(unique_ch)}')
# print(new_string)


string = input().upper()
new_string = ''
unique_ch = ''
text = ''
digits = ''
for index in range(len(string)):
    current_index = index
    ch = string[index]
    if len(digits) > 0 and ch.isdigit():
        digits += ch
        new_string += text * int(digits)
        text = ''
        digits = ''
    if ch.isdigit() and len(digits) == 0:
        digits += ch
        if current_index == len(string) - 1:
            new_string += text * int(digits)
    if not ch.isdigit() and len(digits) > 0:
        new_string += text * int(digits)
        text = ''
        digits = ''
        if ch not in unique_ch:
            unique_ch += ch
    if not ch.isdigit():
        text += ch
        if ch not in unique_ch:
            unique_ch += ch

print(f'Unique symbols used: {len(unique_ch)}')
print(new_string)
