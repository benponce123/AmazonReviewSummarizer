### Amazon Review Summarizer
### Stopwords

# This file contains stopwords_list to take out unnecessary words and characters
# during the weighting and scoring process of this project as these words can
# affect the fairness and relevance of other words.


# Most of the words came from source: https://www.ranks.nl/stopwords
# But the list below is customized to add and remove words that will affect
# the summary and our algorithm
# Words removed from original list: after,again,all,before,few,more,most,
# only,same,than,until,very
# The above words may be relevant in a review as reviewers usually compare
# products and indicate quantity
stopwords_list = ['a','about','above','against','am','an','and','any','are',
                  'aren',"aren't",'as','at','be','because','been','being',
                  'below','between','both','but','by','can',"can't",'cannot',
                  'could','couldn',"couldn't",'d','did','didn',"didn't",'do',
                  'does','doesn',"doesn't",'doing','don',"don't",'down','during',
                  'each','for','from','further','had','hadn',"hadn't",'has',
                  'hasn',"hasn't",'have','haven',"haven't",'having','he',"he'd",
                  "he'll","he's",'her','here',"here's",'hers','herself','him',
                  'himself','his','how',"how's",'i',"i'd","i'll","i'm","i've",
                  'if','in','into','is','isn',"isn't",'it',"it's",'its','itself',
                  'let',"let's",'ll','m','me','mine','mustn',"mustn't",'my','myself',
                  'n','no','nor','not','of','off','on','once','or','other',
                  'ought','our','ours','ourselves','out','over','own','re','s',
                  'shan',"shan't",'she',"she'd","she'll","she's",'should',
                  'shouldn',"shouldn't",'so','some','such','that',"that's",'the',
                  'their','theirs','them','themselves','then','there',"there's",
                  'these','they',"they'd","they'll","they're","they've",'this',
                  'those','through','t','to','too','under','up','ve','was','wasn',
                  "wasn't",'we',"we'd","we'll","we're","we've",'were','weren',
                  "weren't",'what',"what's",'when',"when's",'where',"where's",
                  'which','while','who',"who's",'whom','why',"why's",'with',
                  'won',"won't",'would','wouldn'"wouldn't",'you',"you'd","you'll",
                  "you're","you've",'your','yours','yourself','yourselves',"'d",
                  "'ll","'m","n't","'re","'s","'t","'ve",'.',',','!','?','(',')',
                  '[',']','{','}',"/",'|','@','#','$','%','^','&','*','+','-',
                  '=','~',':',';']
