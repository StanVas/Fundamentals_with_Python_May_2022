import re

text = input()
pattern = r'([|#])(?P<item_name>[A-Za-z\s]+)\1(?P<exp_date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})\1(?P<calories>[0-9]{1,5})\1'
result = re.finditer(pattern, text)
total_calories = 0
food_dict = []    # works with list not dict (with dict gets only 33/100)

for show in result:
    total_calories += int(show['calories'])
    food = show['item_name']
    exp_date = show['exp_date']
    calories = show['calories']
    food_dict.append({'food': food, 'exp_date': exp_date, 'calories': calories})
days_to_last = total_calories // 2000
print(f'You have food to last you for: {days_to_last} days!')
for food in food_dict:
    print(f"Item: {food['food']}, Best before: {food['exp_date']}, Nutrition: {food['calories']}")
