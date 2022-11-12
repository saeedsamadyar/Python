# Dictionaries                     ()Tuples          [] List
# --------------------------------

me = {
    "name": "John",
    "lastname": "Booker",
    "age": 25,
    "Burn": 1989,
    "friends": ['william', 'john', 'philip'],  # list
    "Happy": False  # boolian
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

x = me.values()             #value method
print(x)

print('----------------------------')

y = me.items()              #items method
print(y)

print('----------------------------')

x = "name" in me
print(x)