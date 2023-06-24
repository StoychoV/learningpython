#!/usr/bin/env python3


password = str(input("Please give me the password:\n"))



password_uppercase = False
password_digit = False
password_length_check = False
password_length = len(password)


for char in password:
	if char.isupper():
		password_uppercase = True
	if char.isdigit():
		password_digit = True

if password_uppercase == False:
	print("Make sure that there is at least 1 uppercase letter")

if password_digit == False:
	print("You should use at least 1 digit")

if password_length < 8:
	print("Your password should have at least 8 characters")
else:
	password_length_check = True

if password_uppercase and password_digit and password_length_check:
	print("Password is secure!")


