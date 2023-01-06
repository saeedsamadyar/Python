#
#
# x = lambda a: a + 10              #return
# m = lambda a, b, c: a + b + c
#
# print(m(10, 10, 10))
#
# print('-------------------------------')

# def myfunc(n):
#     def new(a):
#         return a * n
#
#     return new
#
#
# #mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mytripler(2))

print('--------------------------')

#
# def myfunc(n):
#
#     return lambda a: a * n
#
# mydoubler = myfunc(2)
#
# print(mydoubler(5))
#
# print('-------------------------')
#
# mylist = [1, 2, 3, 4, 5, 6, 7, 8]
#
# def myfunction(number):
#     return number * 2
#
# x = map(myfunction, mylist)
# print(list(x))
#
# print('--------------------------')
##Map_Function    Iterable means tuple or list or ...

# mylist = [1, 2, 3, 4, 5, 6, 7, 8]
#
# x = map(lambda a: a * 2, mylist)
#
# print(list(x))
#
# print('----------------------------')
#
# mylist = [1, 2, 3, 4, 5]
# mylist_2 = [2, 3, 4, 6]
#
# x = list(map(lambda a, b: a * b, mylist, mylist_2))         # list is casting
#
# print(x)

# print('------------------------------')

mylist = [1, 2, 3, 4, 5]
b = []

for item in mylist:
    b.append(item * 2)

    print(b)

