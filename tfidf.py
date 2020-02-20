import json
import sys
import os
import read_data
import collections
import math
import nltk
from nltk import word_tokenize

def calculate_tfidf(data):
    '''
    Calculates importance of a term given a review, among other reviews


    Parameter:
    data: list of reviews for a single asin [{reviewerID: str, ...},{}]

    Return:
    tfidf: {reviewerID:{term:tfidf value}, ...} dict of dicts, showing tfidf for each term for each review
    '''
    total_reviews = len(data)
    tfs,idfs, tfidfs = {},{},{}
    term_documents = collections.defaultdict(int)
    for review in data:
        reviewerID = review['reviewerID']
        tfs[reviewerID] = dict()
        tokens = word_tokenize(review['reviewText'].lower())
        total_tokens = len(tokens)
        term_dict = collections.defaultdict(int)
        token_set = set()
        for token in tokens:
            term_dict[token] += 1
            token_set.add(token)
            
        term_dict = dict(term_dict)
        for token, num_tokens in term_dict.items():
            tfs[reviewerID][token] = num_tokens/total_tokens

        for token in token_set:
            term_documents[token] += 1
            
    term_documents = dict(term_documents)
    for token, num_reviews in term_documents.items():
        idfs[token] = math.log(total_reviews/num_reviews)

    for reviewerID, token_dict in tfs.items():
        tfidfs[reviewerID] = {}
        for token, tf in token_dict.items():
            tfidfs[reviewerID][token] = tf * idfs[token]
            
    return tfidfs
        
#product_dict = read_data.load_data()
#for k,v in product_dict.items():
#    tfidfs = calculate_tfidf(v)
#    for reviewerID, tfidf in tfidfs.items():
#        sorted_tfidf = sorted(tfidf.items(), key=lambda x: -x[1])
#        for x in sorted_tfidf:
#            print(x)
#    break
