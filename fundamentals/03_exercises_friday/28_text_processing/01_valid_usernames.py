user_names = input().split(', ')

for user in user_names:
    user_is_valid = True
    if not 3 <= len(user) <= 16:
        user_is_valid = False
    for ch in user:
        if not (ch.isalnum() or ch == '-' or ch == '_'):
            user_is_valid = False
    if ' ' in user:
        user_is_valid = False
    if user_is_valid:
        print(user)
