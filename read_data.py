import json
import sys
import os

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


#d = read_json('reviews_Musical_Instruments_5.json')
#print(d[1])
