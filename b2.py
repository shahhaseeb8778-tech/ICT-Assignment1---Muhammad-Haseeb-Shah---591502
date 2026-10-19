# B2.py  This program calculates total resistance of resistors connected in series
# Formula used: R_total = R1 + R2 + R3 + ...

n= int(input("How many resistors? "))
total_resistance = 0
for i in range(1, n + 1):
    resistor_value = int(input(f"Enter R{i}: "))
    total_resistance = total_resistance + resistor_value
print(f"Total resistance = {total_resistance} ohm")
