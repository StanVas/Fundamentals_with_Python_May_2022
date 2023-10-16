products = {}

while True:
    command = input()
    if command == 'statistics':
        break

    else:
        command = command.split(': ')
        key = command[0]
        value = int(command[1])
        if key in products:
            products[key] += value
        else:
            products[key] = value

print(f'Products in stock:')
products_representation = [f'- {item}: {str(products[item])}' for item in products]
print('\n'.join(products_representation))
print(f'Total Products: {len(products)}')
print(f'Total Quantity: {sum(products.values())}')
