d = {'apple': 1, 'banana': 10, 'orange': 100}

dc = {k: v for k, v in d.items() if v % 2 == 0}
print(dc)
# {'banana': 10, 'orange': 100}

dc = {k: v for k, v in d.items() if v % 2 == 1}
print(dc)
# {'apple': 1}

dc = {k: v for k, v in d.items() if k.endswith('e')}
print(dc)
# {'apple': 1, 'orange': 100}

dc = {k: v for k, v in d.items() if not k.endswith('e')}
print(dc)
# {'banana': 10}

dc = {k: v for k, v in d.items() if v % 2 == 0 and k.endswith('e')}
print(dc)
# {'orange': 100}
########

d = {'k1': 1, 'k2': 2, 'k3': 3}

del d['k1'], d['k3']
print(d)
# {'k2': 2}

##########

d = {'k1': 1, 'k2': 2}

k, v = d.popitem()
print(k)
print(v)
print(d)
# k2
# 2
# {'k1': 1}

k, v = d.popitem()
print(k)
print(v)
print(d)
# k1
# 1
# {}

# k, v = d.popitem()
# KeyError: 'popitem(): dictionary is empty'

###########

d = {'k1': 1, 'k2': 2, 'k3': 3}

removed_value = d.pop('k1')
print(d)
# {'k2': 2, 'k3': 3}

print(removed_value)
# 1

#############

