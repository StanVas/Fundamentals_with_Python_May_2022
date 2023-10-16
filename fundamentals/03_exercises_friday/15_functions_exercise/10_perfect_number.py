def perfect_num(num):
    divisors_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            divisors_sum += divisor
    if num == divisors_sum:
        return "We have a perfect number!"
    return "It's not so perfect."


number = int(input())
print(perfect_num(number))
