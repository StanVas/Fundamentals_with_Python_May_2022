people_waiting = int(input())
state_of_the_lift = list(map(int, input().split()))
number_of_wagons = len(state_of_the_lift)
occupied_space = sum(state_of_the_lift)
free_space = (number_of_wagons * 4) - occupied_space

for current_wagon in range(len(state_of_the_lift)):
    while int(state_of_the_lift[current_wagon]) < 4:
        state_of_the_lift[current_wagon] += 1
        people_waiting -= 1
        if people_waiting == 0:
            break

if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
    print(" ".join([str(x) for x in state_of_the_lift]))
else:
    print("The lift has empty spots!")
    print(" ".join([str(x) for x in state_of_the_lift]))
