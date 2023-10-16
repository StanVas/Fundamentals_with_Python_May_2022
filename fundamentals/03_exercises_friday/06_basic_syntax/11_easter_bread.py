budget = float(input())
price_flour = float(input())
number_of_loaves = 0
colored_eggs = 0
price_eggs = price_flour * 0.75
price_litter_milk = price_flour * 1.25
while budget >= 0:
    one_loaf_price = price_eggs + price_flour + (price_litter_milk * 0.25)
    if budget < one_loaf_price:
        break

    number_of_loaves += 1
    budget -= one_loaf_price
    colored_eggs += 3
    if number_of_loaves % 3 == 0:
        colored_eggs -= (number_of_loaves - 2)

print(f'You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')
