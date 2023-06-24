#!/usr/bin/env python3
#we use this module to take arguments
import sys

#Library we use for regex
import re

#Library we use to send HTTP requests
import requests

#Library used to parse HTML code
from bs4 import BeautifulSoup


#We ask the user to provide us with the URL of the page

page_to_scrape = sys.argv[1]


#page_to_scrape = input("Please provide me with the URL I should scrape: ")

#The function here checks if the provided URL is correct
def is_url(page_to_scrape):
	#The pattern below is used to verify if the URL is correct
	pattern = r"(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"
	match = re.fullmatch(pattern,page_to_scrape)

	if match:
		print("URL is correct. Starting the analysis...")
		return True
	else:
		print("Invalid URL format.")
		return False

#We run the function on the provided URL
is_url(page_to_scrape)

#we get the HTML code from the URL
response = requests.get(page_to_scrape)

#We check if the response code was 200OK
if response.status_code == 200:
	html_content = response.text
else:
	print("Could not scrape the page.")

soup = BeautifulSoup(html_content, "html.parser")

#We look for the name
product_name_element = soup.find('h1', class_="heading left")
product_name = product_name_element.text.strip() if product_name_element else "Product name not available"

#We look for the price
price_element = soup.find('span', itemprop='price')
price = price_element.text.strip() if price_element else "Price not available"


#We look for the short description
short_desc_element = soup.find('div', class_="prod_description left w100")
short_desc = short_desc_element.text.strip() if short_desc_element else "Short description not available"
short_desc  = "\n".join([ll.rstrip() for ll in short_desc.splitlines() if ll.strip()])

# Remove extra spaces at the beginning of each line
short_desc_formatted = re.sub(r"\n\s+", "\n", short_desc)

# Remove warranty lines
short_desc_formatted = re.sub(r"Гаранция \(.*?\)\:.*?\n", "", short_desc_formatted)

short_desc_formatted = re.sub(r"\nслед регистрация", "", short_desc_formatted)

# Format the brand and manufacturer lines
short_desc_formatted = re.sub(r"(Марка|Производител):\s*\n(.+)", r"\1: \2", short_desc_formatted)

# Format the "Размери" line
short_desc_formatted = re.sub(r"Размери: Д/Ш/В -\s+(\d+)\s+/\s+(\d+)\s+/\s+(\d+)\s+mm", r"Размери: Д/Ш/В - \1 / \2 / \3 mm", short_desc_formatted)



#We look for the long description
long_desc_element = soup.find('div', class_="tab_accordeon").ul
#long_desc = long_desc_element.text.strip() if long_desc_element else "Long description not available"
data = [li.get_text(strip=True) for li in long_desc_element.find_all('li')]
long_desc = formatted_output = '\n'.join(data)


# Add separators between blocks
separator = "-" * 40

print(separator)
print("Name: ", product_name)
print(separator)
print("Price:", price)
print(separator)
print("Short Description:")
print(short_desc_formatted)
print(separator)
print("Long Description:")
print(long_desc)
