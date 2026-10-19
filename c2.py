
#C2.py  Parallel Resistance: calculates equivalent resistance of parallel resistors

def parallel_resistance(resistors):
    inverse_sum = 0
    for r in resistors:
        inverse_sum = inverse_sum + (1 / r)
    equivalent_resistance = 1 / inverse_sum
    return equivalent_resistance
resistors1 = [10, 10]
result1 = parallel_resistance(resistors1)
print(f"parallel_resistance({resistors1}) -> {result1}")
resistors2 = [100, 200, 300]
result2 = parallel_resistance(resistors2)
print(f"parallel_resistance({resistors2}) -> {round(result2, 2)}")

