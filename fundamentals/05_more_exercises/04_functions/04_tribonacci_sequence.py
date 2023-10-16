a = 1
b = 1
n = int(input())  # Set this to however many terms you want to generate
series = [1, 1]

for x in range(2, n):
    next = series[x - 1] + series[x - 2] + series[x - 3]
    series.append(next)

print(*series)
