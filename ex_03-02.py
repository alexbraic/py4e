sh = input("Enter hours: ")
sr = input("Enter rate: ")
# try/catch in case input is non-numeric
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please enter a numeric input")
    quit()
# print(fh, fr)
if fh > 40:
    print("Overtime")
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    print("Regular")
    xp = fr * fh
print("Pay:", xp)