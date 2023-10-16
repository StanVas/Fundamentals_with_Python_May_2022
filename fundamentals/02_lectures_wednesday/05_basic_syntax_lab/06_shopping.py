budget = int(input())
command = input()
current_budget = 0
while command != 'End':
    current_budget += int(command)
    if current_budget > budget:
        print("You went in overdraft!")
        break
    command = input()


else:
    print('You bought everything needed.')
