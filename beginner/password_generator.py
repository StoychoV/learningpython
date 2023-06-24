#!/usr/bin/env python3

import string
import random

while True:
	try:
		input_password_length = int(input("Please type how long the password should be. Minimum is 8 characters: "))
		if input_password_length < 8:
			print("Please select a stronger password with 8 or more characters") 
		else:
			break
	except ValueError:
		print("Invalid input. Please enter a valid number")
 
allowed_characters = string.ascii_letters + string.digits + string.punctuation

final_password = ""

for _ in range(input_password_length):
	build_password = random.choice(allowed_characters)
	final_password += build_password

print(f"Your password is:\n{final_password}")
