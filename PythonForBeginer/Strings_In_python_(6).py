#Strings

name = 'william'
familyname = 'boocker'
print('william','booker')

print('---------------------------')

my_name = ('my_name is: '"Johne")
print(my_name)

print('--------------------------')
x = 'I am John\nbooker'
print(x)

print('--------------------------')
my_name = "my name is:", "John boker"
print(my_name)
print("---------------------------")

# SlicingStrings

x = 'most likely'
print(x[2])                #index
print(x[5])
print(x[2:7])
print(x[1:11])
print(x[1:])
print(x[:11])
print(x[-2:-5])

print('----------------------------')

# String Concatenate

name = 'John'
familyname =  'Booker'
city = 'NYC'
# me = name + " " + familyname + " " + city
me = f'{name} {familyname} {city}'              # format String
print(me)

print('----------------------------')

age = '33'
txt = "my age is: " + str(age)
city = 'nyc'
txt = f'{age} {city}'                           #format string
print(txt)

print('---------------------------')

#methods
txt  = "william is from NYC"
# print(txt.capitalize())
# print(txt.count('william is'))
# print(txt.index("i"))
# print(txt.count("wi"))
print(txt.upper())
print(txt.lower())
