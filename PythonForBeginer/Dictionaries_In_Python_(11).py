# Dictionaries                     ()Tuples          [] List         {} Set
# --------------------------------
# first dictionary

me = {
    "name": "John",
    "lastname": "Booker",
    "age": 25,
    "Burn": 1989,
    "friends": ['william', 'john', 'philip'],  # list
    "Happy": False  # boolian
}
# second dictionary
me2 = {
    "name": "saeed",
    "lastname": "s",
    "age": 35,
    "myfriend": ['mojan', 'depi', 'willia', 'jessi']
}
me2 = dict(me)  # copy of me
me2['color'] = 'green'
print(type(me))
print(len(me))
print(me2)

print('---------------------------------')

me = {  # Dictionary
    "name": "william",
    "lastname": "booker",
    "age": 29
}
myname = me["name"]
myage = me["age"]
print(myname)
print(myage)

print('---------------------------')

myname = me.get('name')  # get method
print(myname)

print('---------------------------')

x = me.keys()  # keys method
print(me)

print('-----------------------------')

x = me.values()  # value method
print(x)

print('----------------------------')

y = me.items()  # items method
print(y)

print('----------------------------')

x = "name" in me  # boolian
print(x)

print('----------------------------')

me['age'] = 47  # change value in key
me['Friend'] = "Julia"  # Add key and value in dictionary
me.update({"age": 98})  # change value in key
print(me)

print('-----------------------------')

# me.pop('name')              # remove key
print(me)

print('--------------------------------')

me.popitem()  # remove last item
print(me)

print('--------------------------------')

del me['name']  # remove key
print(me)

me.clear()  # clear dictionaries
print(me)

print('--------------------------------')

# me2 = me.copy()    # copy
# me2['friend'] = 'jack'
# print(me)

print('---------------------------------')

me = dict(me2)  # dict is a function is doing copy of dictionary
me['color'] = 'red'  # add key to dictionary
me['marriage'] = 'single'  # add key to dictionary
print(me)

print('-------------------------------')

# Nested Dictionaries

myfamily = {

    dict: {  # key 1
        "name": 'johnni',
        "lastname": 'mahsoon',
        "age": 28
    },

    dict: {  # key 2
        "name": 'jackson',
        "familyname": 'booker',
        "age": 29
    }
}

    # family2: {                                   # key 2
    # "name": 'jackson',
    # "familyname": 'booker',
    # "age": 29
    # },
    # family2 = dict(family1)
    # print(family1)
print('---------------------------')

myfamily = {
    'child1': {  # Key one
        "name": 'John',  # Item
        "familyname": 'william',
        "age": 38
    },

    'child2': {  # Key two
        "name": 'jesi',  # Item
        "familyname": 'pinkman',

    }

}
myfamily['child1'] = 'Single'
myfamily['child2'] = 'married'

print(myfamily)

# print(myfamily['child1'])
# print(myfamily['child2'])
# print(type('child1'))
