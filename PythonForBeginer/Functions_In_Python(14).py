def me():
    print('Im from United states, loving programming, loving python')


me()

print('----------------------------------')


def my_name(name, lastname):
    print(f"hello {name}{lastname}")
    print(f"how are you? {name}{lastname}?")
    print(f"please give me your info? {name}{lastname}")

    my_name(name="John", lastname="booker")


print("-----------------------------------")


def sum(a, b):     #parametre
    print(a + b)

    sum(a=2, b=4)    #argumant


print("--------------------------------")


def fullname(name, lastname):
    print(f"hello {name} {lastname}")

    fullname(name="john", lastname="willi")


print("---------------------------------")


def callname(fname, lname):
    print(f"{fname} +""+ {lname}")

    callname(fname="jessi", lname="pinkman")


print("--------------------------------")


def callname(fname, lname, *args):  # *arges means tuples
    print(f"hello{fname}{lname}")
    callname("jessi", "pinkman", "willlii")

    print("----------------------------")


def hello(*names):  # *arges Tuples
    for name in names:
        print(f"hello{name}")

        hello("john", "willi", "jessi")

print("------------------------------")

def hello(lname, fname, *name):          #*argesTuples
    print(fname)
    print(lname)
    print(name)          #*arges

hello("john","jessi","alia")
