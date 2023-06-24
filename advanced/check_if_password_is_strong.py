#!/usr/bin/env python3




def password_strength(password):
	#The minimum chars in the password
	minimum_length = 8
	#This will be used to track the strength 
	met_criteria = 0
	#We set this value to False to see if will become True as part of the checks below
	has_uppercase = False
	has_digit = False
	has_special = False

	if len(password) >= minimum_length:  #Less than or equals
		met_criteria += 1
	
	for char in password:
		if char.isupper():  #If there is an upper-case char
			has_uppercase = True
		elif char.isdigit(): #if 0-9
			has_digit = True
		elif not char.isalnum():
			has_special = True


	if has_uppercase:  #If True
		met_criteria += 1
	if has_digit: #if True
		met_criteria += 1
	if has_special: #if True
		met_criteria += 1
	

	if met_criteria < 2:
		pass_strength = "Weak"
	elif met_criteria == 2 or met_criteria == 3:
		pass_strength = "Moderate"
	elif met_criteria == 4:
		pass_strength = "Strong"

	return pass_strength


user_password = input("Please provide me with the password: ")
result = password_strength(user_password)

print(f"Your password is {result}")
