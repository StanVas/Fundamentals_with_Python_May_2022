file_path = input().split('\\')

for element in file_path:
    if '.' in element:
        name, extension = element.split('.')
        print(f'File name: {name}')
        print(f'File extension: {extension}')
