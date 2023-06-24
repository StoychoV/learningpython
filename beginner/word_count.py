#!/usr/bin/env python3


text = str(input("Give text and I will tell the number of words:\n"))

text = text.replace("\n"," ")

count_words = len(text.split())

print(f"You have a total of {count_words} words in your message.")

