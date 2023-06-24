#!/usr/bin/env python3

number = int(input("Provide me with a number and I will tell you if it is a prime one: "))

if number > 1:
	for i in range(2, int(number/2)+1):
		if (number % i) == 0:
			print(f"{number} is not a prime number!")
			break
	else:
		print(f"{number} is a prime number!")
else:
	print(f"{number} is not a prime number!")
