products_lst = input().split()
product_dict = {}

for i in range(0, len(products_lst), 2):
    product_dict[products_lst[i]] = int(products_lst[i + 1])
# dict comprehension
# products_dict = {data[i]: int(data[i + 1]) for i in range(0, len(data), 2)}
print(product_dict)
