#Sets

sets = {'apple','banana','orange','cherry'}
print(type(sets))
print(sets)

print('---------------------------')

myset = {'william','John','Saeed','Booker'}
myset2 = {'Mohammed','Saeed','Julia'}

print('william' in myset)                      #show True or False  (in)

myset.add("James")        #use method
myset.update(myset2)
myset.discard('John')         #remove item of list
#myset3 = myset.union(myset2)
#myset.pop()
#myset.clear()
#del myset                    #delete variable
print(myset)

print('-----------------------------')
set = {1,2,3,4}
set2 = {'a','b','c','d'}
set3 = set2.union(set)
print(set3)









