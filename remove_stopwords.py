import string

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv


def to_text(user):
    csv_file = '%s_tweets.csv' % (user)
    txt_file = '%s_txt.txt' % (user)

    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
        my_output_file.close()

"""
def remove_punction_and_stopwords(msg):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(msg)
    filtered_words = [w for w in msg if w not in word_tokens and w not in string.punctuation]
    new_sentence = ''.join(filtered_words)
    return new_sentence
"""

to_text("bunthebig")
