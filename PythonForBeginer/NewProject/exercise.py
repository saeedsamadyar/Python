sh = input("Enter Hours: ")
sr = input("Enter Rate: ")
fh = input (float (sh))
fr = input (float (sr))

if fh > 40:
    reg = fh * fr
    otp = (fh - 40.0) * (fr * 0.5)
    xp  = reg + otp
else:
    xp = fh * fr
    print("pay: ",xp)