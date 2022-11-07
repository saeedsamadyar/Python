# Tuples

myfriend = ('John','booker','shila','mohammed','saeed')
myfriend = list(myfriend)
print(type(myfriend))
myfriend[1] = 'william'
new_tuple = tuple(myfriend)
print(type(new_tuple))
print(myfriend)

print('-----------------------------')

tuple1 = (1,2,3,4,5,6)
tuple2 = ('william','booker','james','heath')
tuple3 = tuple1 + tuple2
print(tuple3)

