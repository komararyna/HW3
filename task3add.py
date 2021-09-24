a, b, c = int(input('insert first side:')), int(input('insert second side:')), int(input('insert third side:'))
if a < b+c and b < a+c and c < a+b:
    print('it exists')
else:
    print('this triangle doesn`t exist')