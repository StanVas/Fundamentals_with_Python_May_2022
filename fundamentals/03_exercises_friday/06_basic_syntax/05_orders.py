numb_of_orders = int(input())
total_cost = 0
order_cost = 0
for order in range(numb_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif capsules_per_day > 2000 or capsules_per_day < 1:
        continue
    elif days > 31 or days < 1:
        continue
    order_cost = days * capsules_per_day * price_per_capsule
    total_cost += order_cost
    if order_cost != 0:
        print(f'The price for the coffee is: ${order_cost:.2f}')
print(f'Total: ${total_cost:.2f}')
