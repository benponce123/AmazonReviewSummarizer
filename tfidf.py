import collections
import math
import nltk
from nltk import word_tokenize

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

def calculate_tfidf(data):
    '''
    Calculates importance of a term given a review, among other reviews


    Parameter:
    data: list of reviews for a single asin [{reviewerID: str, ...},{}]

    Return:
    tfidf: {reviewerID:{term:tfidf value}, ...} dict of dicts, showing tfidf for each term for each review
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
        tokens = [t for t in tokens if not t in stopwords_list]
        total_tokens = len(tokens)
        term_dict = collections.defaultdict(int)
        token_set = set()
        for token in tokens:
            term_dict[token] += 1
            token_set.add(token)
            
        term_dict = dict(term_dict)
        for token, num_tokens in term_dict.items():
            tfs[reviewerID][token] = num_tokens/total_tokens

        for token in token_set:
            term_documents[token] += 1
            
    term_documents = dict(term_documents)
    for token, num_reviews in term_documents.items():
        idfs[token] = math.log(total_reviews/num_reviews)

    for reviewerID, token_dict in tfs.items():
        tfidfs[reviewerID] = {}
        for token, tf in token_dict.items():
            tfidfs[reviewerID][token] = tf * idfs[token]
            
    return tfidfs
