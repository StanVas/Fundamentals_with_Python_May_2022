level_of_fire = input().split('#')
water = int(input())
cells = []
effort = 0
total_fire = 0
for current_fire in level_of_fire:
    if 'High' in current_fire:
        type_of_fire, range_of_fire = current_fire.split('=')
        range_of_fire = int(range_of_fire)
        if water < range_of_fire:
            continue
        if 81 <= range_of_fire <= 125:
            water -= range_of_fire
            effort += range_of_fire * 0.25
            total_fire += range_of_fire
            cells.append(range_of_fire)
    elif 'Medium' in current_fire:
        type_of_fire, range_of_fire = current_fire.split('=')
        range_of_fire = int(range_of_fire)
        if water < range_of_fire:
            continue
        if 51 <= range_of_fire <= 80:
            water -= range_of_fire
            effort += range_of_fire * 0.25
            total_fire += range_of_fire
            cells.append(range_of_fire)
    elif 'Low' in current_fire:
        type_of_fire, range_of_fire = current_fire.split('=')
        range_of_fire = int(range_of_fire)
        if water < range_of_fire:
            continue
        if 1 <= range_of_fire <= 50:
            water -= range_of_fire
            effort += range_of_fire * 0.25
            total_fire += range_of_fire
            cells.append(range_of_fire)
print('Cells:')
for cell in range(len(cells)):
    print(f' - {cells[cell]}')

print(f'Effort: {effort:.2f}')
print(f'Total Fire: {total_fire}')
