# B5.py  This program sorts 100 ohm resistors into bins by tolerance
# 1%, 5% and reject, loop stops when 0 is entered

count_1_percent = 0
count_5_percent = 0
count_reject = 0
while True:
    measured_resistance = float(input("Enter measured resistance (0 to stop): "))
    if measured_resistance == 0:
        break
    if measured_resistance >= 99.0 and measured_resistance <= 101.0:
        count_1_percent +=1
    elif measured_resistance >= 95.0 and measured_resistance <= 105.0:
        count_5_percent +=1
    else:
        count_reject +=1
print("1% tolerance count:", count_1_percent)
print("5% tolerance count:", count_5_percent)
print("Reject count:", count_reject)

