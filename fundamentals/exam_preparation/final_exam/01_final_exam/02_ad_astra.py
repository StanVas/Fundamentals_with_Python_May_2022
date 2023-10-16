import re

items = input()
# pattern = r'#([A-Za-z\s]+)#([0-9]{2}/[0-9]{2}/[0-9]{2})#([0-9]{1,5})#|' \
#       r'\|([A-Za-z\s]+)\|([0-9]{2}/[0-9]{2}/[0-9]{2})\|([0-9]{1,5})\|'

# pattern = r'#([A-Za-z\s]+)#([0-9]{2}/[0-9]{2}/[0-9]{2})#([0-9]{1,})#|\|)([A-Za-z\s]+)\|([0-9]{2}/[0-9]{2}/[0-9]{2})\|([0-9]{1,})\|'

pattern = r'([#|])([A-Za-z\s]+)\1([0-9]{2}/[0-9]{2}/[0-9]{2})\1([0-9]{1,})\1'
result = re.findall(pattern, items)
food_dict = {}
total_calories = 0
for element in result:
    food = element[1]
    exp_date = element[2]
    calories = element[3]
    food_dict[food] = {'exp_date': exp_date, 'calories': int(calories)}
    total_calories += int(calories)

days_to_last = total_calories // 2000
print(f"You have food to last you for: {days_to_last} days!")
for element in food_dict:
    food = element
    exp_date = food_dict[element]['exp_date']
    calories = food_dict[element]['calories']
    print(f"Item: {food}, Best before: {exp_date}, Nutrition: {calories}")
