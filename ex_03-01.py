# string hour and string rate
sh = input("Enter hours: ")
sr = input("Enter rate: ")

# float hour and float rate
fh = float(sh)
fr = float(sr)

if fh > 40:
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    # print(reg, otp)
    xp = reg + otp
else:
    print("Regular")
    xp = fh * fr
print("Pay:", xp)

