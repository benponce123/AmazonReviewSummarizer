README.txt


Folders:
rouge_evaluation
Contains the methods necessary to calculate ROUGE-N and ROUGE-L for a computer-generated and human made summaries


Modules:
bag_of_words.py
Creates a bag of words for a set of product reviews

key phrases.py
Finds important phrases in a set of product reviews

logistic_classify.py
Creates a logistic regression model that will give weights to each word

read_data.py
Contains helper functions to help in reading the json file

rouge_evaluation.py
Calculates precision, recall, and f-measure for ROUGE-1,2,L to evaluate computer-generated summaries

run_classify.py
Prints the results of logistic_classify.py for testing purposes

run_tfidf.py
Prints the results of tfidf.py for testing purposes

stopwords.py
Contains a list of stop words and irrelevant characters

summary_formation.py
Scores the key phrases and forms summaries

tfidf.py
Calculates the TF-IDF of each token in the review


Others:
human_summaries.txt
Contains human summaries and computer-generated summaries used in rouge_evaluation.py

avgRatings.p
Contains dictionary of average review value for each product

product_reviews.p
Contains dictionary of lists of review data

reviews_Musical_Instruments_5.json
Training data used for the project



