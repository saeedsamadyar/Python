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

# or

print("a") if a > b else print("b")

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

print('-------------------------')

if a == b:
    print('a equal b')
elif a > b:
    print('a is gtreater than b')
else:
    print('Hi my name is john')

print('-------------------------')

a = 10
b = 20
c = 30
if a < b and a != b:
    print('fallen')

print('--------------------------')

# a = 10
# b = 30
# c = 40
# if a < b or != a and a < b:
# print('true')


