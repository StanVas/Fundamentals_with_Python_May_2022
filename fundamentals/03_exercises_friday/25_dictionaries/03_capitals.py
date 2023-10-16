countries = input().split(', ')
capitals = input().split(', ')

result = {countries[i]: capitals[i] for i in range(len(countries))} #  dictionary comprehension

# res1 = dict(zip(countries, capitals)) # zip method
# print(res1)

for country, capital in result.items():
    print(f'{country} -> {capital}')
