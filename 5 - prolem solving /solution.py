
temperatures = [75, 78, 80, 82, 79, 81, 77]

total_sum = sum(temperatures)


average_temperature = total_sum / len(temperatures)

days_above_average = 0

for temp in temperatures:
    if temp > average_temperature:
        days_above_average += 1

print("Average temperature for the week:", average_temperature)
print("Number of days with temperatures above average:", days_above_average)
