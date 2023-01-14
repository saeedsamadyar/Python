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
#
# print('------------------------')
#
#
# class MyClass:
#
#     def __int__(self, name, lastname):
#         self.myname = name
#         self.mylastname = lastname
#
#         p1 = MyClass("John", "pinkman")
#
#         print(p1.myname)
#         print(p1.mylastname)
#
# print('--------------------------')
#
# class personal:
#     def __int__(self, name, lastname, age):
#         self.myname = name
#         self.mylastname = lastname
#         self.myage = age
#
#         p4 = personal("John", "williams", "34")
#
#         print(p4.myname)
#         print(p4.mylastname)
#         print(p4.myage)
#
# print('-----------------------------')
#
# class personal:
#     def __int__(self):
#         print("Hello my world!")
#
#         p1 = personal()  # object
#
#         print(p1)
#
#
# print('---------------------------------')


class MyClass:
    def __int__(self, name, lastname, age):
        self.myname = name
        self.mylastname = lastname
        self.myage = age

def fullname(self):
    #print(f"hey I am {self.myname} {self.mylastname}")
    print(self.myname)
    print(self.mylastname)

    p1 = MyClass("John", "will", "24")    #object

    p1.fullname()
