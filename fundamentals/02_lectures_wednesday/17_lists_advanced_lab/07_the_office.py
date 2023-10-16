employees_happiness = list(map(int, input().split(' ')))
improvement_factor = int(input())
total_employees = len(employees_happiness)
total_happiness = sum(employees_happiness)
average_happiness = total_happiness / total_employees
filtered = list(filter(lambda x: x >= average_happiness, employees_happiness))
happy_employees = len(filtered)
if happy_employees >= total_employees / 2:
    print(f"Score: {happy_employees}/{total_employees}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{total_employees}. Employees are not happy!")
