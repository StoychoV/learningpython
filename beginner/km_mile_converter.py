#!/usr/bin/env python3

distance_input = float(input("What is the distance you are working with: "))

#What is the current format
convert_format = int(input("What is the current format you are using:\n1.Kilometer - KM\n2.Miles - M\nYour choice: "))

#Verify the selection
while convert_format not in [1, 2]:
	print("Invalid choice. Please pick 1 or 2")
	convert_format = int(input("What is the current format you are using:\n1.Kilometer - KM\n2.Miles - M\nYour choice: "))
#User selected kilometers
if convert_format == 1:
	current_format = "Kilometers"
	other_format = "Miles"
	#The formula is X * 0.62137119, where X is the distance
	converted_distance = round(distance_input * 0.62137119, 2)
elif convert_format == 2:
	current_format = "Miles"
	other_format = "Kilometers"
	#The formula is X * 1.609344, where X is the distance
	converted_distance = round(distance_input * 1.609344, 2)

print(f"{distance_input} in {current_format} equals to {converted_distance} in {other_format}")

