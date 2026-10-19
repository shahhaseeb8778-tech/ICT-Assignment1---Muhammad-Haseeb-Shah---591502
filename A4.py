#A4.py  Logic Gates: calculates AND , OR AND XOR outputs for two bits

a = int(input("Enter the value of A : "))
b = int(input("Enter the value of B: "))
if a not in (0, 1) or b not in (0, 1):
    print("Bits must be 0 or 1")
else:
    print("AND:", a & b)
    print("OR:", a | b)
    print("XOR:", a ^ b)
