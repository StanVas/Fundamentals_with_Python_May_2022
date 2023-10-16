num = int(input())
key_word = input()
string_list = []
key_word_list = []

for _ in range(num):
    current_string = input()
    string_list += [current_string]
    if key_word in current_string:
        key_word_list += [current_string]
print(string_list)
print(key_word_list)
