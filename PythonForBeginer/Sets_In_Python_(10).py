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
#myset.pop()
myset.clear()
#del myset                    #delete variable
print(myset)


