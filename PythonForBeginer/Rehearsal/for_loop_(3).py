name = input('Please enter your fullname: ')
name = name.lower()
name = name.replace(" ","")

b =[]
for n in name:
    if n not in b:
        print(f"you name has {name.count(n)} {n}")
        b.append(n)