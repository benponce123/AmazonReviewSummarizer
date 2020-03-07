import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
import json
import sklearn
from sklearn.feature_extraction.text import *
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

stopwords_list = ['a','about','above','against','am','an','and',
                  'any','are',"aren't",'as','at','be','because','been','being',
                  'below','between','both','but','by',"can't",'cannot','could',
                  "couldn't",'did',"didn't",'do','does',"doesn't",'doing',"don't",
                  'down','during','each','for','from','further','had',"hadn't",
                  'has',"hasn't",'have',"haven't",'having','he',"he'd","he'll",
                  "he's",'her','here',"here's",'hers','herself','him','himself',
                  'his','how',"how's",'i',"i'd","i'll","i'm","i've",'if','in',
                  'into','is',"isn't",'it',"it's",'its','itself',"let's",'me',
                  "mustn't",'my','myself','no','nor','not','of','off','on','once',
                  'or','other','ought','our','ours','ourselves','out','over',
                  'own',"shan't",'she',"she'd","she'll","she's",'should',
                  "shouldn't",'so','some','such','that',"that's",'the','their',
                  'theirs','them','themselves','then','there',"there's",'these',
                  'they',"they'd","they'll","they're","they've",'this','those',
                  'through','to','too','under','up','was',"wasn't",'we',"we'd",
                  "we'll","we're","we've",'were',"weren't",'what',"what's",'when',
                  "when's",'where',"where's",'which','while','who',"who's",'whom',
                  'why',"why's",'with',"won't",'would',"wouldn't",'you',"you'd",
                  "you'll","you're","you've",'your','yours','yourself',
                  'yourselves',"n't","'s",'.',',','!','?','(',')','[',']','{','}',"/",
                  '|','@','#','$','%','^','&','*','+','-','=','~']

def logistic_classifier(filename, product, train_test_fraction):
	'''
	Takes in a json file and a specific product ID (asin), separates into
	train/test fraction subsets, and builds a logistic classifier on the data.

	Parameters:
	filename: json file, product: asin, train_test_fraction: fraction to divide train/test data

	Return:
	weight_dict -> {word: weight} for specific product

	'''
	data = [json.loads(review) for review in open(os.path.join(sys.path[0], filename), 'r')]
	print('\nTotal reviews =', len(data))
	weight_dict = dict()
	reviewText = []
	overall_list = []
	specific_review = []
	for review in data:
		review_text = review['reviewText']
		if review['asin'] == product:
			specific_review.append(review_text)
		stars = review['overall']
		if stars != 3:
			if stars >= 4:
				score = 1
			elif stars <= 2:
				score = 0
			reviewText.append(review_text)
			overall_list.append(score)


	vectorizer = CountVectorizer(stop_words=stopwords_list, min_df = 0.02, ngram_range=(1 ,1))
	X = vectorizer.fit_transform(reviewText)

	#Separate data in training and test, build logistic classifier
	X_train, X_test, Y_train, Y_test = train_test_split(X, overall_list, test_size=train_test_fraction, random_state=77)

	print('Number of training examples: ', X_train.shape[0])
	print('Number of testing examples: ', X_test.shape[0])
	classifier = linear_model.LogisticRegression(penalty='l2', fit_intercept=True, solver='lbfgs')
	classifier = classifier.fit(X_train, Y_train)
	train_predictions = classifier.predict(X_train)
	train_accuracy = metrics.accuracy_score(Y_train, train_predictions)

	#calculating training accuracy
	print('\nTraining accuracy:' ,format( 100 *train_accuracy , '.2f'))

	#calculating testing accuracy
	test_predictions = classifier.predict(X_test)
	test_accuracy = metrics.accuracy_score(Y_test, test_predictions)
	print('Testing accuracy:', format( 100 *test_accuracy , '.2f'))

	#calculating auc score
	class_probabilities = classifier.predict_proba(X_test)[: ,1]
	test_auc_score = metrics.roc_auc_score(Y_test, class_probabilities)
	print('AUC value:', format( 100 * test_auc_score , '.2f'))

	specific_review_text = "".join(specific_review)
	specific_list = word_tokenize(specific_review_text)

	#build weight_dict for specific product
	for weight in classifier.coef_[0].argsort()[::-1]:
		current_word = vectorizer.get_feature_names()[weight]
		if current_word in specific_list:
			weight_dict[current_word] = classifier.coef_[0][weight]


	return weight_dict