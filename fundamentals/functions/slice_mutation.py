a = "Test Example"
print(a[0:4])
print(a[5:])
print(a[::-1])
print(a[12:4:-1])

# build_in func - reversed()

# other examples for str
b = "other str"
print(a + b)
print(b * 5)
c = "third str "   # with space
print(c * 3)

d = 'it\'s'
print(d)

e = 5
print('this is number: %d' % e) # without f'string => 'd' for number and 's' for string
print('this is number: {}'.format(e))

f = 'my name is Peter'
name = f[-5:]
name2 = f[11:]
name3 = f[slice(-5, 16, 1)]
print(name, name2, name3)
