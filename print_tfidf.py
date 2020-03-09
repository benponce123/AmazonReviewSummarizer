### Amazon Review Summarizer
### Print TF-IDF

# The purpose of this file is to visualize the calculated tf-idfs from tfidf.py
# so we can analyze it for the next steps of the project.


import os
import json
import nltk
import pickle
from tfidf import calculate_tfidf
from read_data import load_data

if __name__ == '__main__':
        product_dict = load_data()
        avgRatings = pickle.load(open( "avgRatings.p", "rb" ))
        product_list = [items[0] for items in sorted([[key, avgRatings[key]] for key, value in product_dict.items()], key =lambda x: x[1])] # sort descending order by num reviews
        for productID in product_list:
                print('productID: ' + productID + '\n')
                print('avgRatings: ' + str(avgRatings[productID]))
                tfidfs = calculate_tfidf(product_dict[productID])
                #for reviewerID, tfidf in tfidfs.items():
                        #print('reviewerID: ' + reviewerID)
                        #threshold = sum(tfidf.values())/len(tfidf)
                        #sorted_tfidf = sorted([(k,v) for k,v in tfidf.items() if v > threshold], key=lambda x: -x[1]) # excludes term if tfidf is below threshold
                        #for x in sorted_tfidf:
                        #        print(x)
                        #print()
                #break           # stops after first product

