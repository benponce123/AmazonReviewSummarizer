### Amazon Review Summarizer
### Read Data

# This file contains helper functions read_json, separate_data, and load_data
# that will open and read a json file and turn it into a pickle file for easy
# loading and manipulation.


import json
import sys
import os
import pickle
import collections

def read_json(filename):
    '''
    Opens and reads a json file turning it into a list

    Parameter:
    filename: filename of the json file to read

    Return:
    data: list of review data [{reviewerID:str,asin:str,...},{...},...]
    '''
    
    data = [json.loads(review) for review in open(os.path.join(sys.path[0], filename), 'r')]
    return data

def separate_data(data):
    '''
    Separates the review data by asin(product id)
    Stores the review data locally with pickle into product_reviews.p
    
    Parameter:
    data: list of review data from read_json
    
    Return:
    None; creates a pickle file
    '''
    
    product_dict = collections.defaultdict(list)
    for review in data:
        product_dict[review['asin']].append(review)
    product_dict = dict(product_dict)
    pickle.dump(product_dict, open( "product_reviews.p", "wb" ))
            
def load_data():
    '''
    Loads the pickle file from separate_data

    Return:
    Dictionary of lists of review data
    {asin:[{reviewerID:str,asin:str,...},{...}],...}
    '''
    
    return pickle.load(open( "product_reviews.p", "rb" ))


