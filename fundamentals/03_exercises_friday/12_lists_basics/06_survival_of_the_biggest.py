list_of_strings = input().split()
numbers_to_delete = int(input())
list_of_integers = []

for element in list_of_strings:
    list_of_integers.append(int(element))

for num in range(numbers_to_delete):
    min_num = min(list_of_integers)
    list_of_integers.remove(min_num)

#print(', '.join(list_of_integers))
print(*list_of_integers, sep=", ")
