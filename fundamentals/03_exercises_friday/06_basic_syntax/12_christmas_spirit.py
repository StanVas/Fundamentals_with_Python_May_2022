budget = 0
christmas_spirit = 0
quantity_of_decorations = int(input())
days_until_christmas = int(input())
for day in range(1, days_until_christmas + 1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 2 == 0:
        budget += 2 * quantity_of_decorations
        christmas_spirit += 5
    if day % 3 == 0:
        budget += 8 * quantity_of_decorations
        christmas_spirit += 3 + 10
    if day % 5 == 0:
        budget += 15 * quantity_of_decorations
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        budget += 5 + 3 + 15

if days_until_christmas % 10 == 0:
    christmas_spirit -= 30
print(f"Total cost: {budget}")
print(f"Total spirit: {christmas_spirit}")
