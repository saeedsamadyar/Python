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
me_list.append(4)
me_list.append("Julia")
print(me_list)

print('---------------------------')

friendlist = ["John","william","Nik","Nazanin","Booker",]
newfriends = ["Robi","Sofia","mohammed","Roya","Saeed"]
friendlist.insert(2,"Roein")                      #Add Item
newfriends.extend(friendlist)                     #Mix Lists
print(newfriends)
