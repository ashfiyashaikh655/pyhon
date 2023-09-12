current_year=int(input('current_year:'))
joining_year=int(input('joining_year:'))
serve_year=current_year-joining_year
print('serve_year=',serve_year)
if serve_year>3:
    bonus=2500
    print('bonus=',bonus)
else:
    bonus=0
    print('bonus=',bonus)
