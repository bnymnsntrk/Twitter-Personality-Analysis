import string
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv

user = "realdonaldtrump"


def to_text(user):
    csv_file = '%s_tweets.csv' % user
    txt_file = '%s.txt' % user

    with open(txt_file, "w") as output_file:
        with open(csv_file, "r") as input_file:
            [output_file.write(" ".join(row) + '\n') for row in csv.reader(input_file)]
        output_file.close()


def remove_stops(user, time):

    if time == 1:
        txt_in = '%s.txt' % user
        txt_out = '%s_filtered.txt' % user
    else:
        txt_in = '%s_filtered.txt' % user
        txt_out = '%s_final.txt' % user

    stop_words = set(stopwords.words('english'))
    file1 = open(txt_in)
    line = file1.read()  # Use this to read file content as a stream:

    line = line.replace('b\'', '')
    line = line.replace('\'\n', '')
    line = line.replace('\n', ' ')

    words = line.split()
    for r in words:
        if not r in stop_words:
            appendFile = open(txt_out, 'a')
            appendFile.write(r + "\n")
            appendFile.close()


def remove_usernames(user):
    file = '%s_filtered.txt' % user
    with open(file, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if not (i.__contains__("@") | i.__contains__("RT") | i.__contains__("http") | i.__contains__("#")
                    | i.__contains__("&") | i.__contains__("\\n")):
                f.write(i.lower())
        f.truncate()


to_text(user)
remove_stops(user, 1)
remove_usernames(user)
remove_stops(user, 2)
