total_price = lambda a, b: a * b


product = input()
pcs = int(input())
price = 0
if product == 'coffee':
    price = 1.5
elif product == 'water':
    price = 1
elif product == 'coke':
    price = 1.4
elif product == 'snacks':
    price = 2

print(f'{total_price(price, pcs):.2f}')
