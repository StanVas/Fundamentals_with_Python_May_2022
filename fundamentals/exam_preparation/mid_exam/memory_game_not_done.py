def finding_element(index_lst, some_lst):
    first_index = int(index_lst[0])
    second_index = int(index_lst[1])
    if first_index == second_index:
        print("Invalid input! Adding additional elements to the board")
    elif some_lst[first_index] not in range(len(some_lst)) and some_lst[second_index] not in range(len(some_lst)):
        print("Invalid input! Adding additional elements to the board")
    if first_index in range(len(some_lst)) and second_index in range(len(some_lst)):
        if some_lst[first_index] == some_lst[second_index]:
            some_lst.pop(first_index)
            some_lst.pop(second_index)
            print(f"Congrats! You have found matching elements - {first_index}!")
        elif some_lst[first_index] != some_lst[second_index]:
            print("Try again!")

    return some_lst


sequence_of_elements = input().split()
command = input()
current_move = 0
while command != 'end':
    current_move += 1
    command = command.split()
    # first_index = int(command[0])
    # second_index = int(command[1])
    finding_element(command, sequence_of_elements)
    command = input()





