import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], "rouge_evaluation"))

from rouge import *

#REFERENCE - https://github.com/pltrdy/rouge
#This module takes in a computer-generated summary and performs
#ROUGE-N1, ROUGE-N2, and ROUGE-L evaluation on it. For our purposes, ROUGE-1
#is the one we will be looking at. For each evaluation, 3 metrics are calculated.
#'f', 'p', and 'r'.

#'r' calculates recall by (number of overlapping words/total words in human summary).
#'p' calculates precision by (number of overlapping words/total words in computer summary).
#'f' calculates F-measure or F-score, by (2 * Precision * Recall) / (Precision + Recall).

#We will be using the F-score to evaluate the 2 summaries which range from 0.0 to 1.0(perfect).

computer_generated = "the #### transcript is a written version of each day 's cnn student news program use this transcript to he    lp students with reading comprehension and vocabulary use the weekly newsquiz to test your knowledge of storie s you     saw on cnn student news"

human_generated = "this page includes the show transcript use the transcript to help students with reading comprehension and     vocabulary at the bottom of the page , comment for a chance to be mentioned on cnn student news . you must be a teac    her or a student age # # or older to request a mention on the cnn student news roll call . the weekly newsquiz tests     students ' knowledge of even ts in the news"

rouge = Rouge()
scores = rouge.get_scores(computer_generated, human_generated)

print(scores)



