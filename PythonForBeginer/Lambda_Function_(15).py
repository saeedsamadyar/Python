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


def myfunc(n):

    return lambda a: a * n

mydoubler = myfunc(2)

print(mydoubler(5))
