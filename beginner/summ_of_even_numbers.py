#!/usr/bin/env python3


starting_number = int(input("Starting number: "))
ending_number = int(input("Ending number: "))


summ_of_even_numbers = 0

for number in range(starting_number,ending_number + 1):
	if (number%2) == 0:
		summ_of_even_numbers = summ_of_even_numbers + number
print(f"The summ of the even numbers is {summ_of_even_numbers}")
