

stored_password = "123456"

entered_password = input('please enter your password: ')

while entered_password != stored_password:
    entered_password = input('you are wrong, please enter again: ')

    continue

if entered_password == stored_password:
    print('you logged successfully')



