import re

sentence = input()
pattern = r'(www.[A-Za-z0-9\-]+(\.[a-z]{1,}){1,})'
valid_urls = []
while sentence:
    match = re.search(pattern, sentence)
    if match:
        valid_urls.append(match.group())
    sentence = input()

for url in valid_urls:
    print(url)
