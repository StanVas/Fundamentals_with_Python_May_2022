def check_chairs(numbers_of_rooms):
    total_free_chairs = 0
    needed_chairs = 0
    for numbers_of_room in range(1, numbers_of_rooms + 1):
        free_chairs, visitors = input().split()
        difference = len(free_chairs) - int(visitors)
        if difference >= 0:
            total_free_chairs += difference
        else:
            needed_chairs += abs(difference)
            print(f'{abs(difference)} more chairs needed in room {numbers_of_room}')
    return total_free_chairs, needed_chairs


total_rooms = int(input())
total_free_chairs, needed_chairs = check_chairs(total_rooms)
if total_free_chairs >= needed_chairs:
    print(f'Game On, {total_free_chairs} free chairs left')
