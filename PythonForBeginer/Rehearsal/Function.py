# def func(name):
#     ups = 0
#     lows = 0
#     for item in name:
#         if item.isupper():  # method
#             ups += 1
#         elif item.islower():  # method
#             lows += 1
#     else:
#         pass
#
#     print(f"upper Case is:{ups}")
#     print(f"lower Case is:{lows}")
#
#
# while True:
#     name = input("Please enter your name: ")
#     func(name)


#
# print('-------------------------------')

# def numbertype(number):
#     if number % 2 == 0:
#         print("This is an even number")
#     else:
#         print("This is an odd number")
#
# while True:
#     numberOne = int(input("Please enter a number: "))    #Change string to integer
#     numbertype(numberOne)
#
#     print('-----------------------------')
#
def convertor(day, month, year):
    if month > 10:
        birth = year + 622
    elif day > 10 and month == 10:
        birth = year + 622
    else:
        birth = year + 621

print(f"The date of your birthday is: {birth}")

day = int(input("Please enter your day: "))
month = int(input("Please enter your month: "))
year = int(input("Please enter your year: "))

convertor(day, month, year)
