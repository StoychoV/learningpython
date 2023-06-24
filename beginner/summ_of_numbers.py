#!/usr/bin/env python3


numbers = [2, 4, 5, 6, 8, 11, 13, 15]


def calculate_average(list):
	summed = sum(list)
	num_of_entries  = len(list)
	result = summed // num_of_entries
	print(result)

calculate_average(numbers)
