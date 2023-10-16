# colleague from facebook
number_of_lines = int(input())
opened = "("
closed = ")"
brackets = ""
brackets_list = []

for line in range(number_of_lines):
    text = input()
    if opened in text:
        brackets += "open"
    if closed in text:
        brackets += " closed"
    if len(brackets) > 4:  # "open" is 4 char lenght
        if len(brackets) == 11:  # "open closed" is 11 char lenght, that means brackets are balanced
            brackets = ""
            continue
        else:
            brackets_list.append("unbalanced")

if "unbalanced" in brackets_list:
    print("UNBALANCED")
else:
    print("BALANCED")
