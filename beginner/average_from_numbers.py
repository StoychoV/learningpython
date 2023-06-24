#Task: Calculate the average of a list of numbers
#Description:
#Write a Python program that calculates the average of a given list of numbers. The program should take a list of numbers as input and output the average.

def take_user_input():
    while True:
        user_input = input("Please provide me with a list of numbers separated by space: ")
        input_list = user_input.split() #Converts the input into a list
        try:
            numeric_list = [int(num) for num in input_list] #Converts all entries in the list into integers
            return numeric_list
        except ValueError:
            print("Invalid input! Please use numbers only")

input_list = take_user_input()

def calculate_average_number():
    input_len = len(input_list) #How many entrties are in the list
    input_sum = sum(input_list) #Total sum of ints in the list
    print(f"The average number is:", input_sum // input_len)

calculate_average_number()