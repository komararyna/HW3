a, b, c = int(input('insert first number:')), int(input('insert second number:')), int(input('insert third number:'))
if a>b and a>c:
    print(a, 'is the largest')
elif b>c:
    print(b, 'is the largest')
else:
    print(c, 'is the largest')