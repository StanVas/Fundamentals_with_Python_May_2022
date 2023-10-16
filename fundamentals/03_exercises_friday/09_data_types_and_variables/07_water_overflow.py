lines = int(input())

capacity = 255

for liters_of_water in range(lines):
    current_liters = int(input())
    if current_liters > capacity:
        print('Insufficient capacity!')
        continue
    capacity -= current_liters
print(abs(capacity - 255))
