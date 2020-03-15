### Amazon Review Summarizer
### Summary Formation

# This file contains score_phrases that add the weights of each term in the
# phrase resulting in an overall score, and print_summary that prints out the
# formed summary. 


from math import ceil
import nltk
from nltk import word_tokenize
from .read_data import *
from .tfidf import calculate_tfidf
from .logistic_classify import logistic_classifier
from .keyphrases import find_keyphrases
from .stopwords import *


def score_phrases(filename, asin):
    '''
    Sums up the weights of each word using TF-IDF/Logistic Classifier/review title,
    to calculate the score of each phrases

    Parameters:
    filename: filename of the json file to read
    asin: string of the product ID (asin)

    Return:
    scores: dictionary of phrases as keys and list of scores as values
    {phrase:[TF-IDF score, LC score, both score],...}
    '''

    product_dict = load_data()   # {asin:[{reviewerID:str, asin:...},{...},{...}]}
    product_keyphrases = find_keyphrases(filename, asin)   
    tfidfs = calculate_tfidf(product_dict[asin])
    lc = logistic_classifier(filename, asin, 0.6)
    
    scores = dict()   # store the phrase scores into a dictionary to sort later

    for review, reviewerID in enumerate(tfidfs):
        # Get the the title/summary of the Amazon review
        title = word_tokenize(product_dict[asin][review]['summary'].lower())
        title = [t for t in title if t not in stopwords_list]  # title without stopwords

        for phrase in product_keyphrases[review]:
            # Three scores for TF-IDF, LC, and for both
            phrase_score = [0,0,0]
            nonstopword_phrase = [word for word in phrase if word not in stopwords_list]         

            if len(nonstopword_phrase) > 1:
                for word in phrase:
                    if word not in stopwords_list:
                        # Add TF-IDF weights
                        phrase_score[0] += tfidfs[reviewerID][word]
                        # Add LC weights
                        if word in lc:
                            # No negative weights to capture both top pos & neg words
                            phrase_score[1] += abs(lc[word])
                    
                # Add both TF-IDF and LC, then normalize
                phrase_score[2] = (phrase_score[0] + phrase_score[1])/2 
                
                # Divide by length of phrase since longer phrases will have higher scores
                phrase_score[0] = phrase_score[0]/len(phrase)
                phrase_score[1] = phrase_score[1]/len(phrase)
                phrase_score[2] = phrase_score[2]/len(phrase)
                
                # Title resemblance scoring
                # Title words in the phrase receive higher score
                title_length = len(title)
                ntw = 0    # number of title words in the phrase
                if len(title) > 0:   # avoid division by 0
                    for word in phrase:
                        if word in title:
                            ntw += 1
                    phrase_score[0] += ntw/title_length
                    #phrase_score[1] += ntw/title_length
                    phrase_score[2] += ntw/title_length

                # Add phrase and score in dictionary
                scores[' '.join(phrase)] = phrase_score
                
    return scores


def print_summary(filename, asin, method):
    '''
    Sorts the dictionary of scores and forms sentences to create a summary

    Parameters:
    filename: filename of the json file to read
    asin: string of the product ID (asin)
    method: int indicating scoring method used;
        0 for TF-IDF, 1 for Logistic Classifier, 2 for both

    Return:
    summary: string of formed summary depending on the scoring method used
    '''

    scores = score_phrases(filename,asin)

    # Sorted scores by TF-IDF
    sorted_scores = sorted(scores.items(), key=lambda x:-x[1][method])
    summary = ''
    # Length of summary dependent on # of review sentences
    for i in range(ceil(len(sorted_scores)/5)):
        # Capitalize first letter and end with period
        summary += sorted_scores[i][0][0].upper() + sorted_scores[i][0][1:] + '. '

    return summary
    
                
            



