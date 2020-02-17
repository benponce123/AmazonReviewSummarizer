### Amazon Review Summarizer


import os
import json
import nltk

data = [json.loads(line) for line in open('C:/Users/Ben Fresh/Documents/GitHub/AmazonReviewSummarizer/reviews_Musical_Instruments_5.json', 'r')]

unique_products = dict()

#separate into 1429 unique product reviews
for x in data:
	if x['asin'] in unique_products:
		unique_products[x['asin']] += 1
	else:
		unique_products[x['asin']] = 1

#for each review, add word, +1 freq to that unique product
word_freq = dict()
for review in data:
	if review['asin'] not in word_freq:
		word_freq[review['asin']] = dict()  # word, freq dict
	for word in nltk.word_tokenize(review['reviewText'].lower()):
		if word in word_freq[review['asin']]:
			word_freq[review['asin']][word] += 1
		else:
			word_freq[review['asin']][word] = 1


	print(word_freq)

print("Total Unique Products", len(unique_products))

print(unique_products['1384719342'])
print(word_freq['1384719342'])

#for review in data[:5]:
#	print(review['reviewText'])



