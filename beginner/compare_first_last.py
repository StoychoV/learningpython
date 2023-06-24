#!/usr/bin/env python3

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def compare(list):
	if list[0] == list[-1]:
		return True
	else:
		return False
for entry in numbers_x, numbers_y:
	result = compare(entry)
	print(f"{entry} = {result}")

