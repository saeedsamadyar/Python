# Dictionaries                     ()Tuples          [] List         {} Set
# --------------------------------
# first list
me = {
    "name": "John",
    "lastname": "Booker",
    "age": 25,
    "Burn": 1989,
    "friends": ['william', 'john', 'philip'],  # list
    "Happy": False  # boolian
}
# second list
me2 = {
    "name": "saeed",
    "lastname": "s",
    "age": 35,
    "myfriend": ['mojan', 'depi', 'willia', 'jessi']
}

print(type(me))
print(len(me))
print(me)

print('---------------------------------')

me = {
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

me["age"] = 47  # change value in key
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

me = dict(me2)          # dict is a function is doing copy of list
me['colors'] = 'red'
print(me)
