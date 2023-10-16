sides = {}
command = input()
while command != 'Lumpawaroo':
    if "|" in command:
        force_side, force_user = command.split(" | ")
        condition = False
        if force_side not in sides:
            sides[force_side] = []
        for value in sides.items():
            if [force_user] in value:
                condition = True
                break
        if not condition:
            sides[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(' -> ')
        for key, value in sides.items():
            if force_user in value:
                sides[key].pop(value.index(force_user))
                break
        if force_side not in sides:
            sides[force_side] = []
        sides[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")
    command = input()
for key in sides:
    if len(sides[key]) != 0:
        print(f"Side: {key}, Members: {len(sides[key])}")
        values = sides[key]
        for item in values:
            print(f'! {item}')
