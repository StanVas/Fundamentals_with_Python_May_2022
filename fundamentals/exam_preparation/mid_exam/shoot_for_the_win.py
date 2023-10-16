targets = list(map(int, input().split(' ')))
total_shots = 0
command = input()

while command != 'End':
    index = int(command)
    if index < len(targets):
        current_target = targets[index]
        targets[index] = -1
        total_shots += 1
        targets = [i + current_target if i <= current_target and i != -1
                   else i - current_target if i > current_target and i != -1 else i for i in targets]
    command = input()
print(f"Shot targets: {total_shots} ->", *targets, sep=" ")

# from colleagues
#######################################
#
# main_target = [int(n) for n in input().split()]
#
# made_shots = 0
# command = input()
# targets_number = len(main_target) - 1
#
# while command != "End":
#     command = int(command)
#     if targets_number >= command >= 0 and main_target[command] != -1:
#         made_shots += 1
#         target_value = main_target[command]
#         for index, value in enumerate(main_target):
#             if value != -1:
#                 result_between_targets = value - target_value
#                 if value <= target_value:
#                     result_between_targets = value + target_value
#                 main_target[index] = result_between_targets
#         main_target[command] = -1
#
#     command = input()
#
# print(f"Shot targets: {made_shots} ->", *main_target, sep=" ")
#
####################
#
# targets = [int(i) for i in input().split()]
# command = input()
# shot_targets = 0
#
# while command != 'End':
#     target_index = int(command)
#     if target_index < len(targets):
#         target_value = targets[target_index]
#         shot_targets += 1
#         targets[target_index] = -1
#         targets = [
#             i + target_value if i <= target_value and i != -1 else i - target_value if i > target_value and i != 1 else i
#             for i in targets]
#     command = input()
#
# targets_str = [str(i) for i in targets]
# print(f"Shot targets: {shot_targets} -> {' '.join(targets_str)}")