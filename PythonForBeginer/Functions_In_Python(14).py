# def me():
#     print('Im from United states, loving programming, loving python')
#
#
# me()
#
# print('----------------------------------')
#
#
# def my_name(name, lastname):
#     print(f"hello {name}{lastname}")
#     print(f"how are you? {name}{lastname}?")
#     print(f"please give me your info? {name}{lastname}")
#
#     my_name(name="John", lastname="booker")
#
#
# print("-----------------------------------")
#
#
# def sum(a, b):  # parametre
#     print(a + b)
#
#     sum(a=2, b=4)  # argumant
#
#
# print("--------------------------------")
#
#
# def fullname(name, lastname):
#     print(f"hello {name} {lastname}")
#
#     fullname(name="john", lastname="willi")
#
#
# print("---------------------------------")
#
#
# def callname(fname, lname):
#     print(f"{fname} +""+ {lname}")
#
#     callname(fname="jessi", lname="pinkman")
#
#
# print("--------------------------------")
#
#
# def callname(fname, lname, *args):  # *arges means tuples
#     print(f"hello{fname}{lname}")
#     callname("jessi", "pinkman", "willlii")
#
#     print("----------------------------")
#
#
# def hello(*names):  # *arges Tuples
#     for name in names:
#         print(f"hello{name}")
#
#         hello("john", "willi", "jessi")
#
#
# print("------------------------------")
#
#
# def hello(lname, fname, *name):  # *argesTuples
#     print(fname)
#     print(lname)
#     print(name)  # *arges
#
#
# hello("john", "jessi", "alia", "jessi", "julia")
#
# print('---------------------------')
#
#
# def myname(lname, fname, *args, **kwargs):
#     print(lname)
#     print(fname)
#     print(args)  # Tuples
#     print(kwargs)  # Dictionary
#
#     myname("booker", "jessi", "will", "john", age=33, city="nyc", Team="tajbibi")
#
#
# print('-----------------------------')
#
#
# def name(fname="jessi", lname="booker"):
#     print(f"my fullname is: {fname}{lname}")
#
#     name()
#
#
# print('-----------------------------')
#
#
# def name(a):
#     for names in a:
#         print(f"my name is:{names}")
#
#         name("jessi")
#
#
# print("-----------------------------")
#

# def sum(a, b):
#     a += 1
#     b += 3
#     c = 10
#
#     return (a, b)
# result = sum(3, 5)
# for item in result:
#     print(item)
#
#     print('----------------------------')

def sum(a, b):
    return a + b
    result = (sum(12 + 5))
    print(result)


print('-----------------------------')

username = input('Please enter your username: ')


def validation(username):
    if len(username) > 8:  # len character
        return False
    else:
        return True

if validation(username):
    print("Your username is right.! It`s done")

else:
    if username == validation(username):
        print('your entered username is wrong.!')
        username = input('please enter username: ')

# else:
#     print("your username is wrong.!")


# while username != validation(username):
#     username = input('Your entered username is wrong.! please enter username: ')
#     continue
# # else:
#     if username < validation(username):
#         print('your entered username is right.!')
