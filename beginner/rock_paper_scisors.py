#!/usr/bin/env python3
import random
import sys
Rock = 1
Paper = 2
Scissors = 3


selection = int(input("Please select one of the following:\n1.Rock\n2.Paper\n3.Scissors\nYour choice: "))

if selection == 1:
	player_selection = "Rock 🪨"
elif selection == 2:
	player_selection = "Paper 📃"
elif selection == 3:
	player_selection = "Scissors ✂️ "
elif selection > 3:
	print("Invalid choice, please select 1 - 3")
	sys.exit()
	
print(f"You selected {player_selection}")

computer_selection = random.choice([1, 2, 3])

if computer_selection == 1:
        final_computer_selection = "Rock 🪨 "
elif computer_selection == 2:
        final_computer_selection = "Paper 📃"
elif computer_selection == 3:
        final_computer_selection = "Scissors ✂️ "

print(f"The computer selected {final_computer_selection}")


if selection == computer_selection:
	print("We have a tie!")
elif selection == 1:
	if computer_selection == 2:
		print("Paper covers rock. You lose.")
	else:
		print("Rock smashes scissors. You win.")
elif selection == 2:
	if computer_selection == 3:
		print("Scissors cuts paper. You lose.")
	else:
		print("Paper covers rock. You win.")
elif selection == 3:
	if computer_selection == 1:
		print("Rock smashes scissors. You lose.")
	else:
		print("Scissors cuts paper. You win.")
