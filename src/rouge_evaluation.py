# -*- coding: utf-8 -*-
### Amazon Review Summarizer
### Rouge Evaluation

# REFERENCE - https://github.com/pltrdy/rouge
# This module takes in computer and human-generated summaries and perform
# ROUGE-N1 and ROUGE-N2 evaluation.
# For each evaluation, 3 metrics are calculated: 'f', 'p', and 'r'.

# 'r' calculates recall by (number of overlapping words/total words in human summary).
# 'p' calculates precision by (number of overlapping words/total words in computer summary).
# 'f' calculates F-measure or F-score, by (2 * Precision * Recall) / (Precision + Recall).

# We will be using the F-score to evaluate the summaries which range from 0.0 to 1.0(perfect).


import nltk
from nltk import word_tokenize
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], "rouge_evaluation"))
from rouge import *


# Summary per product
computer_generated = "" # insert something here
human_generated = "" # insert something here

# Lower case parameters
computer_generated = computer_generated.lower()
human_generated = human_generated.lower()

# Tokenize human-generated and then join, so both summaries have same structure
human_generated = ' '.join(word_tokenize(human_generated))

# Remove punctuations for more accurate results
punctuations = ".,?!/()"
computer = ''
human = ''
for char in computer_generated:
    if char not in punctuations:
        computer += char
for char in human_generated:
    if char not in punctuations:
        human += char

# Calculate ROUGE scores
rouge = Rouge()
scores = rouge.get_scores(computer, human)
for s in scores:
    for k,v in s.items():
        print(k,v)



