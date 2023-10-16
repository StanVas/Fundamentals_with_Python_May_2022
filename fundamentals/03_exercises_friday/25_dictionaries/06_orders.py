products = {}
command = input()
while command != 'buy':
    if command == 'buy':
        break
    command_lst = command.split(' ')
    product = command_lst[0]
    price = float(command_lst[1])
    quantity = float(command_lst[2])
    if product not in products:
        products[product] = [price, quantity]
    else:
        products[product][1] += quantity
        if products[product][0] != price:
            products[product][0] = price
    command = input()
for key in products.keys():
    price = products[key][0]
    quantity = products[key][1]
    final_price = price * quantity
    print(f'{key} -> {final_price:.2f}')
