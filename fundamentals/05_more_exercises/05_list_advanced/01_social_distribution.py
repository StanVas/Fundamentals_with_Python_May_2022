wealth = list(map(int, input().split(', ')))
minimum_wealth = int(input())
new_lst = []
if sum(wealth) / len(wealth) < minimum_wealth:
    print('No equal distribution possible')

else:
    biggest_num = max(wealth)
    for num in wealth:
        if num < minimum_wealth:
            difference = minimum_wealth - num
            # biggest_num = max(wealth)
            biggest_num -= difference
            num += difference
            new_lst.append(num)
        else:
            new_lst.append(num)
    new_lst[-1] = biggest_num
    print(new_lst)
