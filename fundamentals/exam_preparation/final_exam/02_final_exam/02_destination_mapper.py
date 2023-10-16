import re

travel_locations = input()
pattern = r'=[A-Z][A-Za-z]{2,}=|/[A-Z][A-Za-z]{2,}/'
valid_locations = re.findall(pattern, travel_locations)
travel_points = 0
final_lst = ''
valid_locations = (','.join(valid_locations))
for location in valid_locations:
    for ch in location:
        if ch != '=' and ch != '/':
            final_lst += ch
final_lst = final_lst.split(',')
for destination in final_lst:
    travel_points += len(destination)

print(f"Destinations: {', '.join(final_lst)}")
print(f'Travel Points: {travel_points}')
