key = int(input())
letters = int(input())
message_lst = []
message = []
for letter in range(letters):
    word = input()
    message_lst.append(ord(word) + key)

for num in message_lst:
    message.append(chr(num))

print(''.join(message))
