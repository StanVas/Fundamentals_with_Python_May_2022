# join - works only with string  -- can unpack list!!!!
test = ['a', 'b', 'c']
print('----'.join(test))

# split
some_text = 'a b c d'
my_list = some_text.split(' ')
print(my_list)

# append = add
empty_list = []
empty_list.append(2)
empty_list.append(3)
print(empty_list)

# replace
version = '3.9.9'
version = version.replace('.', '')

# +=
# number_of_courses = int(input())
# courses = []
#
# for i in range(number_of_courses):
#     current_course = input()
#     courses.append(current_course)!!
#     courses += [current_course]
#     courses += current_course
#
# print(courses)

# loop in list
# for
my_list = ['dog', 'cat', 'fish']
for element in my_list:
    print(element, end=' ')

my_list = ['dog', 'cat', 'fish']
for index in range(len(my_list)):
    print(my_list[index], end=' ')
# while
my_list = ['dog', 'cat', 'fish']
i = 0
while i < len(my_list):
    print(my_list[i], end=' ')
    i += 1

my_list = ['dog', 'cat', 'fish']
while my_list:
    print(my_list[0], end=' ')
    current_element = my_list[0]
    my_list.remove(current_element)

# list range
list(range(1, 11))
print(list)

# pop = removes index
a = [1, 2, 3, 4, 5]
a.pop(1)
print(a)

# remove
a = [1, 2, 3, 4, 5]
a.remove(3)
a.remove(1)
print(a)

# in / not in
