#!/usr/bin/env python3

temperature = float(input("Please provide me with the temperature I should convert: "))

input_format_choice = int(input("Please select the current format:\n1. Fahrenheit\n2. Celsius\nYour choice: "))

while input_format_choice not in [1, 2]:
    print("Invalid choice. Please select 1 or 2.")
    input_format_choice = int(input("Please select the current format:\n1. Fahrenheit\n2. Celsius\nYour choice: "))

if input_format_choice == 1:
    temperature_unit = "Fahrenheit"
    other_unit = "Celsius"
    converted_temperature = (temperature - 32) * 5/9
elif input_format_choice == 2:
    temperature_unit = "Celsius"
    other_unit = "Fahrenheit"
    converted_temperature = (temperature * 9/5) + 32

converted_temperature = round(converted_temperature, 2)

print(f"{temperature} in {temperature_unit} is equal to {converted_temperature} in {other_unit}")
