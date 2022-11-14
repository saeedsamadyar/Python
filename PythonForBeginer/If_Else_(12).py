# If else

if True:
    print('helloo')

if False:
    print('Hola')

print('-------------------------')

a = 33
b = 25

if a > b:
    print('a less than b')

print('--------------------------')

if a != b:  # not equal
    print('a not equal b')

if a < b:
    print('a is less than b')

print('--------------------------')

if a != b:  # not equal
    print('a not equal b')
elif a < b:
    print('a is less than b')
elif a > b:
    print('right')

print('--------------------------')

if a != b:  # not equal
    print('a not equal b')
elif a < b:
    print('a is less than b')
else:
    print('right')