### Amazon Review Summarizer
### Run Summarization

# The purpose of this file is to show the results of our computer-generated
# summaries. You should be able to see the product ID, reviewer ID, product
# rating, title of the review, and the text review

# Product: 'productID'
# ----------------------
# Reviewer: 'reviewerID'
# Rating: 'overall'
# Title: 'summary'
# 'reviewText'


from src.read_data import *
from src.summary_formation import *
import warnings
warnings.simplefilter('ignore')


if __name__ == '__main__':

    # Change values below to test for a different file and/or product
    filename = 'src/reviews_Musical_Instruments_5.json'
    asin = 'B00004Y2UT'
    
    # Uncomment below if testing for a new json file
    #data = read_json(filename)
    #separate_data(data)         # creates pickle file
  
    product_dict = load_data()
    summary1 = print_summary(filename,asin,0) # summary based on tfidf
    summary2 = print_summary(filename,asin,1) # summary based on logclassifier
    summary3 = print_summary(filename,asin,2) # summary based on both methods

    print('\n\nProduct: ' + asin)
    print('------------------------------\n')
    for review in product_dict[asin]:
        print('Reviwer: ' + review['reviewerID'])
        print('Rating: ' + str(review['overall']))
        print('Title: ' + review['summary'])
        print(review['reviewText'] + '\n')
    print('------------------------------')

    print('\n\nTF-IDF Summary\n' + summary1)
    print('\n\nLogistic Classifier Summary\n' + summary2)
    print('\n\nCombined Methods Summary\n' + summary3)
    print()
    print()


    
    '''
    # TESTS
    # Check to see top scores
    print('\n\n***FOR TESTING PURPOSES***')
    scores = score_phrases(filename,asin)

    tfidf_scores = sorted(scores.items(), key=lambda x:-x[1][0])
    print('# of sentences: ' + str(len(tfidf_scores)))
    print('\nTF-IDF')
    print('------------------------------')
    for k,v in tfidf_scores:
        print(v[0], k)

    lc_scores = sorted(scores.items(), key=lambda x:-x[1][1])
    print('\n\nLogClass')
    print('------------------------------')
    for k,v in lc_scores:
        print(v[1], k)

    both_scores = sorted(scores.items(), key=lambda x:-x[1][2])
    print('\n\nBoth Methods')
    print('------------------------------')
    for k,v in both_scores:
        print(v[2], k)'''


    
    
