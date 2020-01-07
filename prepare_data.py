from nltk.corpus import stopwords
import csv


def to_text(user):      # this function converst csv into txt
    csv_file = '%s_tweets.csv' % user
    txt_file = '%s.txt' % user

    with open(txt_file, "w") as output_file:
        with open(csv_file, "r") as input_file:
            [output_file.write(" ".join(row) + '\n') for row in csv.reader(input_file)]
        output_file.close()


def remove_stops(user, time):       # this function removes stopwords when time is 2 and
    if time == 1:                   # removes unnecessary characters when time is 1
        txt_in = '%s.txt' % user
        txt_out = '%s_filtered.txt' % user
    else:
        txt_in = '%s_filtered2.txt' % user
        txt_out = '%s_final.txt' % user

    stop_words = set(stopwords.words('english'))        # stopwords from NLTK
    file1 = open(txt_in)
    line = file1.read()  # Use this to read file content as a stream:

    if time == 2:
        with open(txt_in, "r+") as f:
            for l in f:
                appendFile = open(txt_out, 'a')
                for r in l.split():
                    if not r in stop_words:             # if it is a stop word, do not include it
                        appendFile.write(r + ' ')
                appendFile.write('\n')
            appendFile.close()
    else:                                               # remove unnecessary characters
        line = line.replace('b\'', '')
        line = line.replace('b\"', '')
        line = line.replace('\'\n', '\n')
        line = line.replace('\"\n', '\n')
        line = line.replace('RT', '')
        # line = line.replace('\n', ' ')

        for l in line:                                  # write to the output file with lowercasing
            appendFile = open(txt_out, 'a')
            appendFile.write(l.lower())
            appendFile.close()


def remove_usernames(user):                 # this function removes usernames and image links
    file = '%s_filtered.txt' % user
    txt_out = '%s_filtered2.txt' % user
    with open(file, "r+") as f:
        for line in f:
            appendFile = open(txt_out, 'a')
            for i in line.split():
                if not (i.__contains__("@") | i.__contains__("RT") | i.__contains__("http") | i.__contains__("#")
                        | i.__contains__("&") | i.__contains__("\\n")):     # these are the characters we don't want
                    appendFile.write(i + ' ')       # extend it with a whitespace
            appendFile.write('\n')               # if it is a new tweet put a new line

    """with open(file, "r+") as f:          unused loop
        d = f.readlines()
        f.seek(0)
        for i in d:
            if not (i.__contains__("@") | i.__contains__("RT") | i.__contains__("http") | i.__contains__("#")
                    | i.__contains__("&") | i.__contains__("\\n")):
                f.write(i.lower())
        f.truncate()"""
