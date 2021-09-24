year=int(input('insert year:'))
a=year%4
b=year%400
if a==0 or b==0:
    print('366 days in year')
else:
    print('365 days in year')
