class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
command = input()
while command != 'Stop':
    line = command.split(' ')
    sender = line[0]
    receiver = line[1]
    content = line[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    command = input()

indexes = list(map(int, input().split(", ")))
for index in indexes:
    emails[index].send()

for email in emails:
    print(email.get_info())
