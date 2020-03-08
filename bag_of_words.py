### Amazon Review Summarizer
### Bag of Words

# This file contains product_BOW to create a bag of words for each product
# This function was not specifically used in the tfidf.py and
# logistic_classify.py files, but it was used for analyzing the data.


import json
import sys
import os
import nltk
from read_data import read_json

def product_BOW(filename):
	'''
	Creates a bag of words
	Stores each token and its frequency per product

	Parameter:
	filename: filename of the json file to read

	Return:
	word_bag: dictionary with asin as key and dictionary as value with
	term as key and count as value
	{asin:{term:count,...},...}
	'''
	
	data = read_json(filename)

	#for each review, add word, +1 freq to that unique product
	word_bag = dict()
	for review in data:
		if review['asin'] not in word_bag:
			word_bag[review['asin']] = dict()  # word, freq dict
		for word in nltk.word_tokenize(review['reviewText'].lower()):
			if word in word_bag[review['asin']]:
				word_bag[review['asin']][word] += 1
			else:
				word_bag[review['asin']][word] = 1

	return word_bag


