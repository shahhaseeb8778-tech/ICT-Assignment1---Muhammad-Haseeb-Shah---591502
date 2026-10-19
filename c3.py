# C3.py  Decimal to Binary: converts decimal to binary using repeated division by 2

def decimal_to_binary(n):
    if n == 0:
        return "0"
    binary_string = ""
    decimal_number = n
    while decimal_number > 0:
        remainder = decimal_number % 2
        binary_string = str(remainder) + binary_string
        decimal_number = decimal_number // 2
    return binary_string
print(f"decimal_to_binary(10) -> {decimal_to_binary(10)}")
print(f"decimal_to_binary(25) -> {decimal_to_binary(25)}")
