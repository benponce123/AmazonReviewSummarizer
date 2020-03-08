### Amazon Review Summarizer
### Run TF-IDF

# The purpose of this file is to visualize the calculated tf-idfs from tfidf.py
# so we can analyze it for the next steps of the project.


import os
import json
import nltk
from tfidf import calculate_tfidf
from read_data import load_data


if __name__ == '__main__':
        product_dict = load_data()
        #product_list = sorted(product_dict.keys(), reverse = True) # sort descending order by num reviews
        for productID in product_dict:
                print('productID: ' + productID + '\n')
                tfidfs = calculate_tfidf(product_dict[productID])
                for reviewerID, tfidf in tfidfs.items():
                        print('reviewerID: ' + reviewerID)
                        threshold = sum(tfidf.values())/len(tfidf)
                        sorted_tfidf = sorted([(k,v) for k,v in tfidf.items() if v > threshold], key=lambda x: -x[1]) # excludes term if tfidf is below threshold
                        for x in sorted_tfidf:
                                print(x)
                        print()
                break           # stops after first product

