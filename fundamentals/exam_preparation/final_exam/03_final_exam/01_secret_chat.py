message = input()

while True:
    command = input()
    if command == 'Reveal':
        print(f"You have a new text message: {message}")
        break
    else:
        command = command.split(":|:")
        action = command[0]
        if action == 'InsertSpace':
            index = int(command[1])
            message = message[:index] + " " + message[index:]
            print(message)

        elif action == 'Reverse':
            substring = command[1]
            reversed_substring = substring[::-1]
            if substring in message:
                # word_find = message.find(substring)
                # return message[:word_find] + message[word_find + (len(substring)):] + substring[::-1]
                # message = message[:message.rfind(substring)] + message[message.rfind(substring) + len(substring):] + reversed_substring
                message = message[:message.find(substring)] + message[message.find(substring) + len(substring):] + reversed_substring
                print(message)
            else:
                print('error')

        elif action == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            if substring in message:
                message = message.replace(substring, replacement)
                print(message)
