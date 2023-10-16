some_string = 'https://softuni.bg/trainings/live/details?trainingLabId=84'
if some_string.startswith('https'):
    print('This site has SSL certificate')
else:
    print('THis site has NOT SSL certificate')

# startswith - proverqva s kakvo zapochva
# endswith - proverqva s kakvo zavurshva