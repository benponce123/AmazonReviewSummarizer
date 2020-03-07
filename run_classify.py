
from logistic_classify import *

if __name__ == '__main__':

	#classifier takes in json file, asin(productID), train_test_fraction, threshold weight
	print(logistic_classifier('reviews_Musical_Instruments_5.json', "B0009G1E0K", 0.6))



