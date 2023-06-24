#!/usr/bin/env python3
import os
import sys


def clear_terminal():
    if sys.platform.startswith('win'):  # For Windows
        os.system('cls')
    else:  # For Linux and Mac
        os.system('clear')


def play_game():
	user_input = input("What is your secret word? ").lower()
	while True:
		if not user_input.isalpha():
			print("Invalid input. Please enter characters from a-z only.")
			user_input = input("What is your secret word? ").lower()
		else:
			break


	#create a list of the characters in the input
	secret_word = list(user_input)
	#create a list of unique letters from the list
	secret_word_unique_letters = set(secret_word)


	#This is how we build the guessing board
	#create a list used to print to the players
	#The list is filled with _ characters equal to the number of letters in the user_input
	player_board = ["_"] * len(user_input)



	print(f"Your word to guess consists of {len(user_input)} letters.Try to guess the letters.")
	#This is how we give the player the empty board

	#Number of allowed guesses before the game is over
	allowed_guesses = 5

	#The list is used to update the game_board
	indexes = []

	#Tracking the letters we guessed so far
	guessed_letters = []

	clear_terminal()	

	while allowed_guesses > 0:
		#The win condition is to guess all letters in the secret_word_unique_letters list
		if set(guessed_letters) == secret_word_unique_letters:
			print("🏆 You won 🏆")
			print(f"The word was:\n{user_input}")
			restart_game()
		else:
			print(*player_board)
			guess = str(input("What is your guess: ")).lower()
			#if input is not a single a-z letter
			if len(guess) != 1 or not guess.isalpha():
				print("Invalid input. Please use single letters only")
				continue
			elif guess in secret_word_unique_letters:
				#First check if the letter was already guessed
				if guess not in guessed_letters:
					print("✅ Your guess was correct!")

					#Get the index of the correct letter from the secret_word list and update the index on the player_board one
					indexes = [i for i, item in enumerate(secret_word) if item == guess]
					for index in indexes:
						player_board[index] = guess
					#The correct guess is added to the list of guessed_letters
					guessed_letters.append(guess)

				else:
					print(f"The letter {guess} was already guessed. Please try with a different letter.")
			else:
				#Decrement the number of allowed_guesses by 1
				allowed_guesses -= 1 
				if allowed_guesses == 0:
					print("💀 You lost 💀")
					print(f"The word was {user_input}. Better luck next time!")
					return
				else:
					print(f"💩 Wrong answer! You have {allowed_guesses} guesses left.")

def restart_game():
	while True:
		restart_input = input("Do you want to restart? (yes/no): ").lower()
		if restart_input == "yes":
			play_game()
		elif restart_input == "no":
			print("Thanks for playing!")
			exit()
		else:
			print("Invalid input. Please enter 'yes' or 'no'.")	


play_game()
restart_game()
