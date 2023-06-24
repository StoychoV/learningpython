#!/usr/bin/env python3

user_input = str(input("Give me a string: "))

len = len(user_input)

for i in range(0, len -1, 2):
	print(f"{[i]} {user_input[i]}")
