'''A library charges a fine for every book returned late. For first
5 days the fine is 50 paise, for 6-10 days fine is one rupee and
above 10 days fine is 5 rupees. If you return the book after 30
days your membership will be cancelled. Write a program to
accept the number of days the member is late to return the
book and display the fine or the appropriate message'''

days=int(input('days:'))
if days>=1 and days<=5:
    print('fine is 50 paisa')
elif days>=6 and days<=10:
    print('fine is 1 rupees')
elif days>10 and days<=30:
    print('fine is 5 rupees')
elif days>30:
    print('your membership will be cancelled')
else:
    print('enter valid data')
