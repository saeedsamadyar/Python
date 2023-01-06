# class MyClass:
#     x = 2  # Prpperty
#     y = 4  # property
#
#
# p1 = MyClass()  # Objest1
# p2 = MyClass()  # Object2
#
# print(p1.x)
# print(p2.y)

print('------------------------')


class MyClass:

    def __int__(self, name, lastname):
        self.myname = name
        self.mylastname = lastname

        p1 = MyClass("John", "pinkman")

        print(p1.myname)
        print(p1.mylastname)
