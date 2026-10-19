# B3.py  This program analyzes sensor voltage readings to find count above 3.2V,
# highest reading, lowest reading and average using a single loop

readings = (3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count_above = 0
highest_voltage = readings[0]
lowest_voltage = readings[0]
total_voltage = 0
for voltage in readings:
    if voltage > 3.2:
        count_above += 1
    if voltage > highest_voltage:
        highest_voltage = voltage
    if voltage < lowest_voltage:
        lowest_voltage = voltage
    total_voltage += voltage
average_voltage = total_voltage / 7
print("Readings above 3.2 V:",count_above)
print("Highest:", highest_voltage, "V")
print("Lowest:",lowest_voltage, "V")
print("Average:",round(average_voltage, 2),"V")
