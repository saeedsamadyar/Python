
def passwordvalidation(password):
    if len(password) < 8:
        print("your password must be at least 8 character")
    elif password.isnumric():
        print("your password must have one number")
    elif password.isalpha():
        print("your pasword must have at least one letter")
    else:
        print("your password is currect")


        while True:
            password = ("Please enter your password:" )
            passwordvalidation(password)
