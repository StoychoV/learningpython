encoded_text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def shift_letter(letter):
    if letter.isalpha():
        ascii_value = ord(letter.lower())
        shifted_ascii_value = (ascii_value - 97 + 2) % 26 + 97
        return chr(shifted_ascii_value)
    else:
        return letter

# Apply the shift_letter function to decode the text
decoded_text = "".join(shift_letter(char) for char in encoded_text)

print(decoded_text)

url = "map"

decoded_url = "".join(shift_letter(char) for char in url)
print(decoded_url)