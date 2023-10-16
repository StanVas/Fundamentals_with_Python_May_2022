number_of_lines = int(input())
synonyms = {}

for i in range(number_of_lines):
    word = input()
    synonym = input()
    if word not in synonyms:
        synonyms[word] = []
    synonyms[word].append(synonym)

for word in synonyms:
    print(f'{word} - {", ".join(synonyms[word])}')

### Mario ###
# from collections import defaultdict
# synonyms = defaultdict(list)
# number = int(input())
# for _ in range(number):
#     word, synonym = input(), input()
#     synonyms[word].append(synonym)
# data = [f'{word} - {", ".join(synonym)}' for word, synonym in synonyms.items()]
# print('\n'.join(data))