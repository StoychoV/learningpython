#!/usr/bin/env python3

print("Let's calculate the average of three numbers\n")

num1 = int(input("What is the first number?\n"))

num2 = int(input("What is the second number?\n"))

num3 = int(input("What is the third number?\n"))

result = (num1+num2+num3)/3
int_result = int(result)
print(f"The average is: {int_result}")
