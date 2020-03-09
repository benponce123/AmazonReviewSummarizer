### Amazon Review Summarizer
### TF-IDF

# This file contains calculate_tfidf that creates a bag of words and then
# calculates the term frequency * inverse document frequency of each token
# per review of a specific product.


import collections
import math
import nltk
from nltk import word_tokenize
from stopwords import *


def calculate_tfidf(data):
    '''
    Calculates importance of a term given a review, among other reviews

    Parameter:
    data: list of review data for a single asin from load_data
    [{reviewerID:str,...},{...}]

    Return:
    tfidfs: dict of dicts storing tfidf for each term for each review
    {reviewerID:{term:tfidf value,...},...}
    '''
    
    total_reviews = len(data)
    tfs,idfs, tfidfs = {},{},{}
    term_documents = collections.defaultdict(int)
    for review in data:
        reviewerID = review['reviewerID']
        tfs[reviewerID] = dict()
        s = review['reviewText'].lower()

        # Add space after '.' since some reviewers forget to,
        # e.g.: This is affordable.I like it
        ps = '' 
        for i in range(len(s)-1):
            if s[i] == '.' and s[i+1] != ' ':
                ps += s[i] + ' '
            else:
                ps += s[i]
        ps += s[-1]

        tokens = word_tokenize(ps)
        tokens = [t for t in tokens if not t in stopwords_list] # remove stopwords
        total_tokens = len(tokens)
        term_dict = collections.defaultdict(int)
        token_set = set()
        for token in tokens:
            term_dict[token] += 1
            token_set.add(token) # bag of words
            
        term_dict = dict(term_dict)
        for token, num_tokens in term_dict.items():
            tfs[reviewerID][token] = num_tokens/total_tokens # calculate tf

        for token in token_set:
            term_documents[token] += 1
            
    term_documents = dict(term_documents)
    for token, num_reviews in term_documents.items():
        idfs[token] = math.log(total_reviews/num_reviews) # calculate idf

    for reviewerID, token_dict in tfs.items():
        tfidfs[reviewerID] = {}
        for token, tf in token_dict.items():
            tfidfs[reviewerID][token] = tf * idfs[token] # calculate tf-idf
            
    return tfidfs



