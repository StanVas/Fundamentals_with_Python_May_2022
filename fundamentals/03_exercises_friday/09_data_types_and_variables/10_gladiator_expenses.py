lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_broken_helmets = lost_fights_count // 2 * helmet_price
total_broken_swords = lost_fights_count // 3 * sword_price
total_broken_shields = lost_fights_count // 6 * shield_price
total_broken_armors = lost_fights_count // 12 * armor_price
total_expenses = total_broken_helmets + total_broken_swords + total_broken_shields + total_broken_armors

print(f"Gladiator expenses: {total_expenses:.2f} aureus")
