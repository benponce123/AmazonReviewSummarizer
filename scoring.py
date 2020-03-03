### Key Phrase Scoring

import nltk
from read_data import *
from tfidf import calculate_tfidf
from keyphrases import find_keyphrases


# source: https://www.ranks.nl/stopwords
# words removed from original list: after,again,all,before,few,more,most,
#    only,same,than,until,very
stopwords_list = ['a','about','above','against','am','an','and',
                  'any','are',"aren't",'as','at','be','because','been','being',
                  'below','between','both','but','by',"can't",'cannot','could',
                  "couldn't",'did',"didn't",'do','does',"doesn't",'doing',"don't",
                  'down','during','each','for','from','further','had',"hadn't",
                  'has',"hasn't",'have',"haven't",'having','he',"he'd","he'll",
                  "he's",'her','here',"here's",'hers','herself','him','himself',
                  'his','how',"how's",'i',"i'd","i'll","i'm","i've",'if','in',
                  'into','is',"isn't",'it',"it's",'its','itself',"let's",'me',
                  "mustn't",'my','myself','no','nor','not','of','off','on','once',
                  'or','other','ought','our','ours','ourselves','out','over',
                  'own',"shan't",'she',"she'd","she'll","she's",'should',
                  "shouldn't",'so','some','such','that',"that's",'the','their',
                  'theirs','them','themselves','then','there',"there's",'these',
                  'they',"they'd","they'll","they're","they've",'this','those',
                  'through','to','too','under','up','was',"wasn't",'we',"we'd",
                  "we'll","we're","we've",'were',"weren't",'what',"what's",'when',
                  "when's",'where',"where's",'which','while','who',"who's",'whom',
                  'why',"why's",'with',"won't",'would',"wouldn't",'you',"you'd",
                  "you'll","you're","you've",'your','yours','yourself',
                  'yourselves',"'s",'.',',','!','?','(',')','[',']','{','}',"/",
                  '|','@','#','$','%','^','&','*','+','-','=','~']

def score_phrases(filename, asin):
    '''

    '''
    #data = read_json(filename)
    #separate_data(data)

    product_dict = load_data()
    product_keyphrases = find_keyphrases(filename, asin)
    tfidfs = calculate_tfidf(product_dict[asin])
    scores = dict()

    print(tfidfs)

    for review, reviewerID in enumerate(tfidfs):
        #print(review, reviewerID)
        #print(product_keyphrases[review])
        #print(tfidfs[reviewerID])
        #print()

        for phrase in product_keyphrases[review]:
            print(phrase)
    


score_phrases('reviews_Musical_Instruments_5.json', '1384719342')




