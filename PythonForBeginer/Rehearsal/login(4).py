users = {  # dictionary
    "william": "123",
    "john": "321",
    "jessi": "456",
}

entered_username = input('Please enter your username: ')
entered_password = input('Please enter your password: ')

while entered_username in users and users[entered_username] == entered_password:
    print('congrats, you are our user')


else:

   if entered_username in users and users[entered_username] != entered_password:
        print('sorry, you are not our user, Try again:', entered_password)



