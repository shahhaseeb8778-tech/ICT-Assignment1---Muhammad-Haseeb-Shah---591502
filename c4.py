# C4.py  Loaded Voltage Divider: calculates unloaded and loaded voltage

def loaded_divider(vs, r1, r2, rl):
    unloaded_voltage = vs * r2 / (r1 + r2)
    parallel_resistance = (r2 * rl) / (r2 + rl)
    loaded_voltage = vs * parallel_resistance / (r1 + parallel_resistance)
    return (round(unloaded_voltage, 1), round(loaded_voltage, 1))
result = loaded_divider(12, 1000, 1000, 500)
print(f"loaded_divider(12, 1000, 1000, 500) -> {result}")
result2 = loaded_divider(9, 1000, 2000, 1000)
print(f"loaded_divider(9, 1000, 2000, 1000) -> {result2}")