from read_data import read_json
import nltk
from nltk import word_tokenize, pos_tag


def find_keyphrases(filename, asin):
    '''
    Finds the key phrases of each review,
    which will be used later for sentence scoring

    Parameter:
    filename: filename of the json file containing products and reviews
    product: string of the product ID (asin)

    Return:
    product_keyphrases: nested list of split string key phrases of each review in the product,
                        key phrases start with an adjective or noun and includes
                        the following words and stops with an adjective or noun.
    '''
    product_tokpos = list() 
    
    data = read_json(filename)
    for d in data:
        if d['asin'] == asin:  # find the product
            s = d['reviewText'].lower()  # grab the review text

            # Add space after '.' since some reviewers forget to,
            # e.g.: This is affordable.I like it
            ps = '' 
            for i in range(len(s)-1):
                if s[i] == '.' and s[i+1] != ' ':
                    ps += s[i] + ' '
                else:
                    ps += s[i]
            ps += s[-1]

            tokens = word_tokenize(ps)  # grab the words
            tokens_and_tags = nltk.pos_tag(tokens, tagset='universal')

            #print()
            #print()
            #print(tokens_and_tags)
            

            i = 0
            found_adjnoun = False
            review_keyphrases = list()  # list of key words/phrases in one review
            while (i < len(tokens_and_tags)):

                while found_adjnoun and i < len(tokens_and_tags):
                    if tokens_and_tags[i][1] == '.':
                        review_keyphrases.append(tokens_and_tags[i])
                        found_adjnoun = False
                    elif (tokens_and_tags[i][1] == 'NOUN' or tokens_and_tags[i][1] == 'ADJ'):
                        review_keyphrases.append(tokens_and_tags[i])
                        found_adjnoun = False
                    else:
                        review_keyphrases.append(tokens_and_tags[i])
                    i += 1
                if i < len(tokens_and_tags):
                    if tokens_and_tags[i][1] == '.' and len(review_keyphrases) > 0:
                        if review_keyphrases[-1][1] != '.':
                            review_keyphrases.append(tokens_and_tags[i])
                    
                    if (tokens_and_tags[i][1] == 'NOUN' or tokens_and_tags[i][1] == 'ADJ'):
                        if not review_keyphrases:
                            review_keyphrases.append(tokens_and_tags[i])
                        elif review_keyphrases and (review_keyphrases[-1][1] != 'NOUN' or review_keyphrases[-1][1] != 'ADJ'):
                            review_keyphrases.append(tokens_and_tags[i])
                        found_adjnoun = True
                    i += 1

            #print()
            #print(review_keyphrases)
            
            product_tokpos.append(review_keyphrases)

    product_keyphrases = list()
    for pt in product_tokpos:
        keyphrases = list()
        phrases = ''
        for token,pos in pt:
            if pos == '.':
                keyphrases.append(phrases.split())
                phrases = ''
            else:
                phrases += token + ' '
        product_keyphrases.append(keyphrases)
    
    return product_keyphrases

#find = find_keyphrases('reviews_Musical_Instruments_5.json','1384719342')
#for f in find:
    #print(f)
    #print()




