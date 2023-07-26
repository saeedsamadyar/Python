name = input('Please enter your fullname: ')
name = name.lower()
name = name.replace(" ","")
name = name.strip()

b =[]          #list
for n in name:
    if n not in b:
        print(f"your name has {name.count(n)} {n}")
        b.append(n)
