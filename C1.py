#C1.py  Current and Power: calculates current I=V/R and power = i^2*R

def ohms_current(v, r):
    current = v / r
    return current
def power_dissipated(i, r):
    power = i ** 2 * r
    return power
voltage = 12
resistance = 6
current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)
print(f"Current = {current} A")
print(f"Power = {power} W")
