from read_data import read_json
import nltk
from nltk import word_tokenize, pos_tag


def find_noun_adj(filename, product):
    '''
    Finds the nouns and adjectives of each review per product,
    which will be used later for sentence scoring

    Parameter:
    filename: filename of the json file containing products and reviews
    product: string of the product ID (asin)

    Return:
    product_noun_adj: list of nouns, adjectives, and punctuations in each review
        punctuations are kept to separate sentences and phrases
    
    '''
    product_noun_adj = list() 
    
    data = read_json(filename)
    for d in data:
        if d['asin'] == product:  # find the product
            s = d['reviewText'].lower()  # grab the review text
            tokens = word_tokenize(s)  # grab the words
            tokens_and_tags = nltk.pos_tag(tokens, tagset='universal')

            review_noun_adj = list()  # list of nouns, adj, . per review
            for tt in tokens_and_tags:
                if (tt[1] == 'NOUN' or tt[1] == 'ADJ' or tt[1] == '.'):
                    review_noun_adj.append(tt)

            product_noun_adj.append(review_noun_adj)
    return product_noun_adj

#find = find_noun_adj('1384719342')
#for f in find:
    #print(f)
    #print()




