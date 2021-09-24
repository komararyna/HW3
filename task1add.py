kv = int(input('insert your flat number:'))
if 0 < kv <= 36:
    a = kv % 4
    b = kv / 4
    if a == 0:
        print('подъезд:4', 'этаж:', int(b))
    else:
        print('подъезд:', a, 'этаж:', int(b + 1))
else:
    print('error')
