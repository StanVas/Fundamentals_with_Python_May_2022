# not working properly
text = input().split(' ')
for element in text:
    if ':' in element:
        if len(element) > 2:
            element = element[0] + element[1]
            print(element)
        else:
            print(element)

# from colleague
# main_text = input()
#
# for index, letter in enumerate(main_text):
#     if ":" == letter:
#         print(f"{letter}{main_text[index+1]}")
