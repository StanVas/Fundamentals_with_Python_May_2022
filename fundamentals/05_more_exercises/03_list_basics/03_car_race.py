time_lst = list(map(int, input().split()))
time_len = len(time_lst)
middle_index = int((time_len - 1) / 2)
left_racer = time_lst[:middle_index]
right_racer = time_lst[middle_index + 1:]
right_racer = right_racer[::-1]
right_racer_time = 0
left_racer_time = 0
for num in left_racer:
    if num != 0:
        left_racer_time += num
    elif num == 0:
        left_racer_time *= 0.8

for num in right_racer:
    if num != 0:
        right_racer_time += num
    elif num == 0:
        right_racer_time *= 0.8

if right_racer_time > left_racer_time:
    print(f"The winner is left with total time: {left_racer_time:.1f}")
else:
    print(f"The winner is right with total time: {right_racer_time:.1f}")
