# B4.py  This program finds longest continuous streak of strictly decreasing voltage readings

voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
longest_start_index = 0
longest_length = 1
current_start_index = 0
current_length = 1
for i in range(1, len(voltages)):
    current_voltage = voltages[i]
    previous_voltage = voltages[i-1]
    if current_voltage < previous_voltage:
       current_length = current_length + 1
    else:
        if current_length > longest_length:
            longest_length = current_length
            longest_start_index = current_start_index
        current_start_index = i
        current_length = 1
if current_length > longest_length:
    longest_length = current_length
    longest_start_index = current_start_index
longest_end_index = longest_start_index + longest_length - 1
start_voltage = voltages[longest_start_index]
end_voltage = voltages[longest_end_index]
print("Longest continuous drop:", longest_length, "minutes")
print("Started at:", start_voltage, "V")
print("Ended at:", end_voltage, "V")
