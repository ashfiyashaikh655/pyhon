health=input('health:')
age=int(input('age:'))
lives=input('lives:')
gender= input('gender:')
if health=='excellent' and age>=25 and age<=35 and lives=='city' and gender=='male':
    print('premimum is 4 per thousand')
elif health=='excellent' and age>=25 and age<=35 and lives=='city' and gender=='female':
    print('premimum is 3 per thousand')
elif health=='poor' and age>=25 and age<=35 and lives=='village' and gender=='male':
    print('premimum is 2 per thousand')
else:
    print('enter valid data')
