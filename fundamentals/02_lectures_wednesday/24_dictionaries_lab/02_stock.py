products_lst = input().split()
product_dict = {}

for i in range(0, len(products_lst), 2):
    product_dict[products_lst[i]] = int(products_lst[i + 1])

products_to_search = input().split()

for product in products_to_search:
    if product in product_dict:
        print(f"We have {product_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
