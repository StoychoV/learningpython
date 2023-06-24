#!/usr/bin/env python3

import this

shifted_alphabet = this.d

def decode_text(encoded_text):
	decoded_text = ''
	for char in encoded_text:
		if char in shifted_alphabet:
			decoded_text += shifted_alphabet[char]
		else:
			decoded_text += char
	return decoded_text


encoded_text = this.s

decoded_text = decode_text(encoded_text)

print(decoded_text)	
