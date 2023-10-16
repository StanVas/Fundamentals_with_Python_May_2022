import re

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
bought_furniture = []
total_cost = 0
purchase_info = input()
while purchase_info != 'Purchase':
    result = re.search(pattern, purchase_info)
    if result:
        furniture, price, quantity = result.groups()
        bought_furniture.append(furniture)
        total_cost += int(quantity) * float(price)
    purchase_info = input()
print("Bought furniture:")
for furniture in bought_furniture:
    print(furniture)

print(f'Total money spend: {total_cost:.2f}')
