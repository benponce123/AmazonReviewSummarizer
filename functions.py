import json
import sys
import os
import nltk

def read_json(filename):
	'''
	Converts the json file into a list.

	Parameter:
	filename: filename of the json file to read

	Return:
	data: list of reviews
	'''

	data = [json.loads(review) for review in open(os.path.join(sys.path[0], filename), 'r')]
	return data


#d = read_json('reviews_Musical_Instruments_5.json')
#print(d[1])

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
	word_freq = dict()
	for review in data:
		if review['asin'] not in word_freq:
			word_freq[review['asin']] = dict()  # word, freq dict
		for word in nltk.word_tokenize(review['reviewText'].lower()):
			if word in word_freq[review['asin']]:
				word_freq[review['asin']][word] += 1
			else:
				word_freq[review['asin']][word] = 1
	return word_freq
