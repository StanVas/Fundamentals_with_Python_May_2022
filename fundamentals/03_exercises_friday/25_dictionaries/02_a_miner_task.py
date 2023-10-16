resources = {}

while True:
    current_resource = input()
    if current_resource == 'stop':
        break
    else:
        quantity = int(input())
    if current_resource not in resources.keys():
        resources[current_resource] = quantity
    else:
        resources[current_resource] += quantity

for resource in resources:
    print(f'{resource} -> {resources[resource]}')
