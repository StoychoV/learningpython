#!/usr/bin/env python3
previous_number = 0
for current_number in range(10):
	sum = previous_number + current_number
	print(f"Current Number: {current_number} # Previous: {previous_number} # Sum: {sum}")
	previous_number = current_number
	current_number += 1
