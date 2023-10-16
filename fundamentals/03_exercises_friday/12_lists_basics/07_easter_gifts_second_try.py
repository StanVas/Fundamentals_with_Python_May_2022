names_of_the_gifts = input().split()
command_to_buy = True
while command_to_buy:
    command = input()
    if command == 'No Money':
        command_to_buy = False
        break
    event_info = command.split()
    type_of_event = event_info[0]
    gift = event_info[1]
    if type_of_event == 'Required':
        index = int(event_info[2])
        if 0 < index < len(names_of_the_gifts):
            names_of_the_gifts[index] = gift
    if type_of_event == 'OutOfStock':
        for i in range(len(names_of_the_gifts)):
            if names_of_the_gifts[i] == gift:
                names_of_the_gifts[i] = 'None'
    if type_of_event == 'JustInCase':
        names_of_the_gifts.pop()
        names_of_the_gifts.append(gift)

for gifts in range(len(names_of_the_gifts)):
    if 'None' in names_of_the_gifts:
        names_of_the_gifts.remove('None')
print(*names_of_the_gifts, sep=" ")
