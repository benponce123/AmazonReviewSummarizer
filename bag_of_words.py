import json
import sys
import os
import nltk
import read_data

def product_BOW(filename):
	'''
	Takes in 1 product and returns a bag of words with frequencies.

	Parameter:
	filename: filename of the json file to read

	Return:
	data: Dictionary of unique products and their reviews with dict of term, freq.
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
