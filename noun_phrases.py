import json


data = [json.loads(line) for line in open('/Users/angelicatoledo/Documents/GitHub/AmazonReviewSummarizer/reviews_Musical_Instruments_5.json', 'r')]

print(data[0])
