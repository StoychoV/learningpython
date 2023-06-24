#!/usr/bin/env python3

word = str(input("Give word and I tell:\n"))

word = word.replace(" ","")

word = word.lower()
reversed_word = ''.join(reversed(word))

if word == reversed_word:
	print(f"The word {word} is a palindrome.")
else:
	print(f"The word {word} is NOT a palindrome")

#print(f"Your word is {word}")
#print(f"The reversed is {reversed_word}")
