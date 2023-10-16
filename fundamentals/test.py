gifts = input().split()
command = input().split()
while command[0] != 'No' and command[1] != 'Money':
    if 'OutOfStock' in command:
        while command[1] in gifts:
            index = gifts.index(command[1])
            gifts.remove(command[1])
            gifts.insert(index, "None")
    if 'Required' in command:
        if int(command[2]) < len(gifts):
            gifts.pop(int(command[2]))
            gifts.insert(int(command[2]), command[1])
    if 'JustInCase' in command:
        gifts.pop(-1)
        gifts.append(command[1])
    command = input().split()
for gift in gifts:
    if gift != 'None':
        print(gift, end=' ')
