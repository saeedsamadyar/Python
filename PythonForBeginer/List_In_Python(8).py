#list

my_list = ['apple','orange','banana']
print(my_list)

print ('-----------------------------')

mylist = ['John','william','Kris','Sarah',3,True]
numbers = [1,2,3,4]
print(type(mylist))
print(mylist)
print(mylist[2])
print(len(mylist))
print(numbers)

print('-------------------------------')

name = "John Booker"
print(len(name))

print('-------------------------------')

melist = ["John","James","Sarah","William","Sofia"]
#print(melist[2])
#print(type(melist[2]))
print(melist[3:6])
print(melist[2:])
print(melist[-1])
print(melist[-3:-1])
# ---------------------------------------------
print("----------------------------------------")
# change List Items

mylist = ["Black","Red","Curple","orange","yellow","white"]
print(len(mylist))
mylist[2] = ["red"]
mylist[1:3] = ["white"]
print(len(mylist))
print(mylist)

print('-------------------------------')

All_list = ["John","william","Nik","Nazanin","Booker",]
print(len(All_list))
All_list[1:3] = ["saeed"],["kan"]
All_list.insert(3, "kamdin")
print(len(All_list))
print(All_list)

print('---------------------------------')

me_list = ["John","william","Nik","Nazanin","Booker",]
me_list.append(True)
me_list.append(4)          #Add Item
me_list.append("Julia")
print(me_list)

print('---------------------------')

friendlist = ["John","william","Nik","Nazanin","Booker",]
newfriends = ["Robi","Sofia","mohammed","Roya","Saeed"]
friendlist.insert(2,"Roein")                      #Add Item
newfriends.extend(friendlist)                     #Mix Lists
print(newfriends)

print('-----------------------------')

frinds = ["James","william","Jone"]
frinds.remove("Jone")                 #remove Item
#frinds.pop(1)                        #index
#or
del frinds[1]                         #index
frinds.clear()                        #clear all list
print(frinds)

print('----------------------------')
#sort list

myfriends = ['Jaan','willian','jessi','saeed']
print(myfriends)
numbers = [22,29,87,23,27]
print(numbers)
myfriends.sort()
numbers.sort()
numbers.sort(reverse=True)
print(myfriends)
print(numbers)

print('-----------------------------')

firstlist = ["John","william","Nik","Nazanin","Booker",]
secondlist = ["Robi","Sofia","mohammed","Roya","Saeed"]
firstlist = secondlist.copy()            #copy list
print(firstlist)

print('-----------------------------')

first_list = ["John","william","Nik","Nazanin","Booker",]
second_list = [0,1,2,3,4,5,6,7,8,9]
last_list = first_list + second_list
print(type(first_list))
print(last_list)

