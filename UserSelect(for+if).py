users = {'Oliver': 'male', 'NewYear': 'female', 'Minnie': 'female',
         'Tom': 'male', 'Abby': 'female', 'Bii': 'male', 'Julia': 'female', 'Nok': 'male'}
for name, status in users.copy().items():
    if status == 'male':
        print(name+' : male')
for name, status in users.copy().items():
    if status == 'female':
        print(name+' : female')


for name, status in users.copy().items():
    x = str(input("Please enter here: "))
    if x == 'male':
        for name, status in users.copy().items():
            if status == 'male':
                print(name + ' : male')
    elif x == 'female':
        for name, status in users.copy().items():
            if status == 'female':
                print(name + ' : female')
