company_users = {}

while True:
    command = input()
    if command == 'End':
        break
    company_name, user = command.split(' -> ')
    if company_name not in company_users:
        company_users[company_name] = []
    if user not in company_users[company_name]:
        company_users[company_name].append(user)

for company in company_users:
    print(f'{company}')
    for user in company_users[company]:
        print(f'-- {user}')
