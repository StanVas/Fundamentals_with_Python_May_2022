tasks = []

while True:
    to_do_notes = input().split('-')

    if to_do_notes[0] == 'End':
        break

    priority = int(to_do_notes[0])
    task = to_do_notes[1]
    tasks.append((priority, task))

sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)
