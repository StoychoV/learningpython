#!/usr/bin/env python3


number = int(input("Enter a number and I will tell you its factorial: "))


factorial = 1

if number < 0:
	print("Please enter a positive number")
elif number == 0:
	print("The factorial of 0 is 1")
else:
	for i in range(1,number + 1):
		factorial = factorial*i
#print("The factorial of",number,"is",factorial)
print(f"The factorial of {number} is {factorial}.")
