#!/usr/bin/env python3

import string

allowed_input = string.digits

user_input = input("Enter a list of digits: ")


if not user_input:
	print("No input provided. Please enter a list of digits.")
	exit()

input_list = user_input.split()

for char in input_list:
	if not char.isdigit():
		print("Invalid input. Please enter a list of digits ONLY!")
		exit()
	
digits_list = [int(char) for char in input_list]

print("Valid input. Generating list of digits...")
print("List of digits:",digits_list) 

unique_numbers = list(set(digits_list))
print("Unique numbers:", unique_numbers)
