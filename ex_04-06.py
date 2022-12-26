def computePay(h, r):
    h = float(hrs)
    r = float(rate)
    if h > 40:
        # calculate regular pay
        reg_p = r * 40.0
        # get the overtime hours (over 40)
        xtra_h = h - 40.0
        # calculate overtime rate
        xtra_r = r / 100 * 50
        # calculate the overtime pay and total
        extra_p = xtra_h * (r + xtra_r)
        total_p = reg_p + extra_p
        # return the overtime pay
        return total_p
    # return the regular pay
    return h * r


hrs = input("Enter Hours:")
rate = input("Enter rate:")
p = computePay(hrs, rate)
print("Pay", p)
