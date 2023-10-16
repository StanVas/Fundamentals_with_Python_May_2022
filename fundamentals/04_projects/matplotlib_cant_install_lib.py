x = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y = []
for i in x:
    ex = i ** 3
    y.append(ex)


import matplotlib.pyplot as plt

plt.plot(x, y)

coordinates = list(zip(x, y))
print(coordinates)
