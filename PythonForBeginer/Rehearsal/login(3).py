# friends = ['', '', '', '']  # list

users = {  # dictionary
    "william": "123",
    "john": "321",
    "jessi": "456",
}

entered_username = input('Please enter your username: ')
entered_password = input('Please enter your password: ')

if entered_username in users:
    print('congrats, you are our user')

else:
    print('sorry, you are not our user')

# print(users['william'])          #Show value of key

print('--------------------------------')
print('--------------------------------')
