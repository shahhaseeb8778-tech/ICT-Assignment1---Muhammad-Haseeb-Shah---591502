#A5.py  Smallest and largest resistors: find smallest and largest of three resistors.
resistor1 = float(input("Enter first value of resistor: "))
resistor2 = float(input("Enter second value of resistor: "))
resistor3 = float(input("Enter third value of resistor: "))
if resistor1 <= resistor2 and resistor1 <= resistor3:
    smallest = resistor1
elif resistor2 <= resistor1 and resistor2 <= resistor3:
    smallest = resistor2
else:
    smallest = resistor3
if resistor1 >= resistor2 and resistor1 >= resistor3:
    largest = resistor1
elif resistor2 >= resistor1 and resistor2 >= resistor3:
    largest = resistor2
else:
    largest = resistor3
print("Smallest resistor:", smallest,"ohm")
print("Largest resistor:", largest,"ohm")
