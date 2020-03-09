import json
import sys
import os
import pickle
import collections

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

def separate_data(data):
    '''
    Separate json by asin(product id). Store locally with pickle
    into product_reviews.p
    
    Parameter:
    data: json of reviews
    
    Return:
    None
    '''
    product_dict = collections.defaultdict(list)
    for review in data:
        product_dict[review['asin']].append(review)
    product_dict = dict(product_dict)

    avgRatings = collections.defaultdict(int)
    for productID, reviews in product_dict.items():
        sumRatings = 0
        numReviews = 0
        for review in reviews:
            numReviews += 1
            sumRatings += review['overall']
        avgRatings[productID] = sumRatings/numReviews
        avgRatings = dict(avgRatings)
    
    pickle.dump(product_dict, open( "product_reviews.p", "wb" ))
    pickle.dump(avgRatings, open("avgRatings.p", "wb"))
            
def load_data():
    '''
    Load pickle file

    Return: dict of lists of reviews. {asin:[[],[],]}
    '''
    return pickle.load(open( "product_reviews.p", "rb" ))
<<<<<<< Updated upstream
    
d = read_json('reviews_Musical_Instruments_5.json')
separate_data(d)
#product_dict = load_data()
#for k, v in product_dict.items():
#    print(k,v)
=======

>>>>>>> Stashed changes
