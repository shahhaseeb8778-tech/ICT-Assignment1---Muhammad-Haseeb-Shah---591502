# A1.py  Fuse Check using Ohms Law: calculates current and checks fuse

voltage = float(input("Enter the  voltage(V): "))
resistance = float(input("Enter  the resistance(ohm): "))
if resistance <= 0:
    print("Invalid resistance")
else:
    current = voltage / resistance
    print("Current =", current, "A")
    if current > 2:
        print("Fuse will blow")
    else:
        print("Circuit is safe")
