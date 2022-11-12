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
#set = set.update(set2)
print(set3)

print('-----------------------------')

my_set = {"a","b","c","d","IBM","apple"}
my_set2 = {"Microsoft","IBM","apple"}
my_set3 = my_set.intersection_update(my_set)              #update
my_set.symmetric_difference_update(my_set2)
print(type(my_set2))
print(my_set3)




print('-----------------------------')

my_set = {"a","b","c","d","IBM","apple"}
my_set1 = {"Microsoft","IBM","apple"}
print(my_set | my_set1)

print('------------------------------')












