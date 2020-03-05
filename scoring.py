### Key Phrase Scoring

import nltk
from nltk import word_tokenize
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
                  'yourselves',"n't","'s",'.',',','!','?','(',')','[',']','{','}',"/",
                  '|','@','#','$','%','^','&','*','+','-','=','~']


def score_phrases(filename, asin):
    '''

    '''
    # Uncomment below if testing for a new json file
    #data = read_json(filename)
    #separate_data(data)   # creates pickles file

    product_dict = load_data()   # {asin: [{reviewerID:..., asin:...},{...},{...}]}
    product_keyphrases = find_keyphrases(filename, asin)   
    tfidfs = calculate_tfidf(product_dict[asin])
    scores = dict()   # store the phrase scores into a dictionary to sort later

    for review, reviewerID in enumerate(tfidfs):
        #print(review, reviewerID)
        #print(product_keyphrases[review])
        #print(tfidfs[reviewerID])
        #print()

        # Get the the title/summary of the Amazon review
        title = word_tokenize(product_dict[asin][review]['summary'].lower())
        title = [t for t in title if t not in stopwords_list]
        #print(title)

        for phrase in product_keyphrases[review]:
            phrase_score = 0
            nonstopword_phrase = [word for word in phrase if word not in stopwords_list]         

            if len(nonstopword_phrase) > 1:
                for word in phrase:
                    if word not in stopwords_list:
                        phrase_score += tfidfs[reviewerID][word]   # Add weights

                # Divide by length of phrase since longer phrases will have higher scores
                phrase_score = phrase_score/len(phrase) #len(nonstopword_phrase)

                # Title words in the phrase receive higher score
                title_length = len(title)   # how many words in the title without stopwords
                ntw = 0    # number of title words in the phrase
                if len(title) > 0:   # avoid division by 0
                    for word in phrase:
                        if word in title:
                            ntw += 1
                    #print('ntw',ntw)
                    phrase_score += ntw/title_length

                # Add phrase and score in dictionary
                scores[' '.join(phrase)] = phrase_score

                #print(phrase_score)
                #print(len(phrase))
                #print()

    # Sort the dictionary in descending scores
    sorted_scores = sorted(scores.items(), key=lambda x: -x[1])
    for k,v in sorted_scores:
        print(k, ':', v)

    print(len(sorted_scores))

    return sorted_scores
                
            
    
product_dict = load_data()
print()
print('------------------------------')
print()
for r in product_dict['B000068NSX']:
    print(r['reviewerID'], ':', r['summary'])
    print(r['reviewText'])
    print()
    print()
score_phrases('reviews_Musical_Instruments_5.json', 'B000068NSX')




