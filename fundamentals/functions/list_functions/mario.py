string = input().split()
result = [word * len(word) for word in string]
print(''.join(result))
