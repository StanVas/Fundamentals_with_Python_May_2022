import re

destinations = input()
pattern = r'([\/=])([A-Z][A-Za-z]{2,})\1'
result = re.findall(pattern, destinations)
destination_lst = []
travel_points = 0

for city in result:
    destination_lst.append(city[1])
    travel_points += len(city[1])

print(f'Destinations: {", ".join(destination_lst)}')
print(f'Travel Points: {travel_points}')
