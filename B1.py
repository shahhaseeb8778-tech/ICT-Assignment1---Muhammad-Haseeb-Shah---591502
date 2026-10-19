# B1.py  This program prints current through a 10 ohm resistor 
# for voltages from 1V to 10V using Ohm's Law (I = V/R)

resistance = 10  
for voltage in range(1, 11):
    current = voltage / resistance
    print(f"V = {voltage} V, I = {current} A")
