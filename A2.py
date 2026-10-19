#A2.py  Current Direction: checks direction of current flow

current = float(input("Enter the  current: "))
if current > 0:
    print("Current flows from A to B")
elif current < 0:
    print("Current flows from B to A")
else:
    print("No current flows")
