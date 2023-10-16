text = input()
counter = 0

text_lower = text.lower()
if "sand" in text_lower:
    counter += 1
if "water" in text_lower:
    counter += 1
if "fish" in text_lower:
    counter += 1
if "sun" in text_lower:
    counter += 1

print(counter)
