#!/usr/bin/env python3


number = int(input("Provide me with the number of terms for the Fibonacci sequence: "))

# Initialize the first two numbers of the sequence
fibonacci_sequence = [0, 1]

# Generate the Fibonacci sequence
for i in range(2, number):
    # Calculate the next number by summing the previous two numbers
    next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
    fibonacci_sequence.append(next_number)

# Print the generated Fibonacci sequence
print("Fibonacci sequence:")
for number in fibonacci_sequence:
	print(number, end=" ")

print()

