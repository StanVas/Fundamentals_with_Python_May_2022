# import re
# names = input()
# regex = r"\b[A-Z][a-z]{2,}+\b"
# matches = re.findall(regex, names)
#
# print(" ".join(set(matches)))

import re

names = input()
search_pattern = r"\b([A-Z][a-z]+ [A-Z][a-z]+)\b"
matches = re.findall(search_pattern, names)
print(' '.join(matches))
