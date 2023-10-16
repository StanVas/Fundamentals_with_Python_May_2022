items_to_buy = input().split('|')
budget = float(input())
lst_of_items = []

for item in items_to_buy:
    type_of_item, price_of_item = item.split('->')
    price_of_item = float(price_of_item)
    if price_of_item > budget:
        continue
    if type_of_item == 'Clothes':
        if price_of_item > 50:
            continue
        else:
            budget -= price_of_item
            lst_of_items.append(price_of_item)
    elif type_of_item == 'Shoes':
        if price_of_item > 35:
            continue
        else:
            budget -= price_of_item
            lst_of_items.append(price_of_item)
    elif type_of_item == 'Accessories':
        if price_of_item > 20.50:
            continue
        else:
            budget -= price_of_item
            lst_of_items.append(price_of_item)

profit_lst = []

for element in lst_of_items:
    element += element * 0.4
    element = float(element)
    profit_lst.append(element)

profit_lst = ['%.2f' % elem for elem in profit_lst]
new_list = []
for item in profit_lst:
    new_list.append(float(item))
sum_new_list = sum(new_list)
profit = sum_new_list - sum(lst_of_items)

print(*profit_lst)
print(f'Profit: {profit:.2f}')
if sum_new_list + budget >= 150:
    print(f'Hello, France!')
else:
    print(f'Not enough money.')
