### Amazon Review Summarizer
### Run Logistic Classifier

# The purpose of this file is to visualize the calculated weights of the logistic
# classifier from logistic_classify.py so we can analyze it for the next steps of
# the project.


from logistic_classify import *
import warnings
warnings.simplefilter('ignore')


if __name__ == '__main__':

	# Classifier takes in json file, asin(productID), train_test_fraction
	lc = logistic_classifier('reviews_Musical_Instruments_5.json', "1384719342", 0.6)
	for k,v in lc.items():
                print(v,'\t',k)



