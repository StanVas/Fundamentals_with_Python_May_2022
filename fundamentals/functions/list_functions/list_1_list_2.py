my_list_1 = [1, 2, 3, 4, 5, 6, ]
# my_list_2 = my_list_1 # removes form both
my_list_2 = my_list_1.copy()
my_list_2.pop()
print(my_list_2)
print(my_list_1)