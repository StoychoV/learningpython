#!/usr/bin/env python3

import datetime

print("How long before you turn 100?")

current_datetime = datetime.datetime.now()

current_year = current_datetime.year

name = str(input("What is your name?\n"))

age = int(input("How old are you?\n"))


amount_to_add = 100 - age

year_to_100_yo = current_year + amount_to_add

print(f"You will turn 100 in the year of {year_to_100_yo}")


