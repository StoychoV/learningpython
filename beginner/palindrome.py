#!/usr/bin/env python3

word = str(input("Give word and I tell:\n"))
word = word.lower()

if word == word[::-1]:
	print(f"The word {word} is a palindrome.")
else:
	print(f"The word {word} is NOT a palindrome")

#print(f"Your word is {word}")
#print(f"The reversed is {reversed_word}")
