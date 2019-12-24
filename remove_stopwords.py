import string
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv


def to_text(user):
    csv_file = '%s_tweets.csv' % user
    txt_file = '%s_txt.txt' % user

    with open(txt_file, "w") as my_output_file:
        with open(csv_file, "r") as my_input_file:
            [my_output_file.write(" ".join(row) + '\n') for row in csv.reader(my_input_file)]
        my_output_file.close()


def remove_stops(user):
    txt_in = '%s_txt.txt' % user
    txt_out = '%s_filtered.txt' % user
    stop_words = set(stopwords.words('english'))
    file1 = open(txt_in)
    line = file1.read()  # Use this to read file content as a stream:
    words = line.split()
    for r in words:
        if not r in stop_words:
            appendFile = open(txt_out, 'a')
            appendFile.write("\n"+r)
            appendFile.close()


"""
def remove_punction_and_stopwords(msg):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(msg)
    filtered_words = [w for w in msg if w not in word_tokens and w not in string.punctuation]
    new_sentence = ''.join(filtered_words)
    return new_sentence
"""

to_text("bunthebig")
remove_stops("bunthebig")
