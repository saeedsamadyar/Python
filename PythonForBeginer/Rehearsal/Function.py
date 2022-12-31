def func(name):
    ups = 0
    lows = 0
    for item in name:
        if item.isupper():  # method
            ups += 1
        elif item.islower():  # method
            lows += 1
    else:
        pass

    print(f"upper Case is:{ups}")
    print(f"lower Case is:{lows}")

name = input("Please enter your name: ")

func(name)
