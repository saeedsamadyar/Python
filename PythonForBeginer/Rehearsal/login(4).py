users = {  # dictionary
    "william": "123",
    "john": "321",
    "jessi": "456",
}

entered_username = input('Please enter your username: ')
entered_password = input('Please enter your password: ')

# if entered_username in users and users[entered_username] == entered_password:
#     print('congrats, you are our user')
#
# else:
#
#         print('sorry, you are not our user')

print('---------------------------------')

while entered_username not in users or users[entered_username] != entered_password:
    print('your username and password is wrong')
    entered_username = input('Please enter your username:')
    entered_password = input('Please enter your password:')

else:

    if entered_username in users and users[entered_username] == entered_password:
        print('You loged in.')
#
# else:
#
#     if entered_username in users and users[entered_username] == entered_password:
#         print('you right.!')
