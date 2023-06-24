#!/usr/bin/env python3


numbers = [2, 4, 5, 6, 8, 11, 13, 15]


def calculate_average(list):
	sum_of_all_numbers = sum(list)
	num_of_entries  = len(list)
	result = sum_of_all_numbers // num_of_entries
	print(result)

calculate_average(numbers)
