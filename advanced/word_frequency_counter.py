#!/usr/bin/env python3

import matplotlib.pyplot as plt
import seaborn as sns
import re
from wordcloud import WordCloud



user_input = input("Please provide me with a text to analyze:\n")

punc_clean = re.sub(r'[^\w\s]', '', user_input)
to_lower = punc_clean.lower()
split_text = to_lower.split()

#Defines common words to ignore
common_words = ['the', 'and', 'a', 'of', 'in', 'to', 'is', 'that']



def count_word_frequencies(result):
	word_freq = {}
	total_words = 0 #This variable keeps track of the total number of words
	
	for word in result:
		if word not in common_words: #Ignore common words
			total_words += 1
			if word in word_freq:
				word_freq[word] += 1
			else:
				word_freq[word] = 1

	#Calculate the percentage of each word
	for word in word_freq:
		word_freq[word] = (word_freq[word] / total_words) * 100

	return word_freq

count_result = count_word_frequencies(split_text)
sorted_result = sorted(count_result.items(), key=lambda x: x[1], reverse=True)

#Create a bar chart
def top_words_chart(sorted_result, top_n):
	# Extract the top N most frequent words
	top_words = sorted_result[:top_n]

	# Extract word labels and frequencies
	word_labels = [word for word, _ in top_words]
	word_frequencies = [count for _, count in top_words]

	# Create a bar plot using Matplotlib
	plt.figure(figsize=(10, 6))
	sns.barplot(x=word_frequencies, y=word_labels)

	# Add frequency labels on top of each bar
	for i, (frequency, label) in enumerate(zip(word_frequencies, word_labels)):
		plt.text(frequency + 0.001, i, f"{round(frequency, 1)}%", va='center', ha='right', color='black', fontweight='bold')

	plt.xlabel("% Frequency")
	plt.ylabel("Words")
	plt.title(f"Top {top_n} Most Frequent Words")
	plt.show()


#Create a wordcloud	
def top_words_cloud(sorted_result):

	# Create a string of word-frequency pairs for generating the word cloud
	word_cloud_text = " ".join([f"{word}: {count:.2f}%" for word, count in sorted_result])

	# Generate the word cloud
	wordcloud = WordCloud(width=800, height=400, background_color="white").generate(word_cloud_text)

	# Plot the word cloud using Matplotlib
	plt.figure(figsize=(10, 6))
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.title("Word Cloud")
	plt.show()

program_mode = int(input("What mode do you wish to use:\n1.Chart\n2.Word Cloud\nYour choice: "))

while program_mode not in [1, 2]:
	print("Invalid choice. Please select 1 or 2.")
	program_mode = int(input("What mode do you wish to use:\n1.Chart\n2.Word Cloud\nYour choice: "))
if program_mode == 1:
	top_n = int(input("Enter the number of top words to display: "))
	top_words_chart(sorted_result, top_n)
elif program_mode == 2:
	top_words_cloud(sorted_result)
