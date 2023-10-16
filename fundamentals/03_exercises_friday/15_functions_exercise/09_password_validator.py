def pass_length(some_sting):
    if 6 <= len(some_sting) <= 10:
        return True
    print("Password must be between 6 and 10 characters")
    return False


def only_letters_digits(some_string):
    if some_string.isalnum():
        return True
    print("Password must consist only of letters and digits")
    return False


def at_least_two_digits(some_string):
    digit_counter = 0
    for character in some_string:
        if character.isdigit():
            digit_counter += 1
    if digit_counter >= 2:
        return True
    print("Password must have at least 2 digits")
    return False


some_password = input()
validated = [pass_length(some_password), only_letters_digits(some_password), at_least_two_digits(some_password)]

if all(validated):
    print('Password is valid')
