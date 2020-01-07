from nltk.corpus import twitter_samples
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import FreqDist
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize
import re
import string
import random
import prepare_data

account = "realdonaldtrump"     # <------ write the username here
prepare_data.to_text(account)           # convert to text
prepare_data.remove_stops(account, 1)   # remove unnecessary characters
prepare_data.remove_usernames(account)  # remove usernames and links
prepare_data.remove_stops(account, 2)   # remove stopwords
with open('realdonaldtrump_final.txt', 'r') as file:        # <----- and here, before _final
    data = file.read()

stop_words = stopwords.words('english')     # english is the language we work with


def remove_noise(tweet_tokens, stop_words = ()):        # removing unnecessary characters from NLTK dataset

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())        # no punctuations, and all lower case
    return cleaned_tokens


positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')   # importing dataset
negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

positive_cleaned_tokens_list = []
negative_cleaned_tokens_list = []

for tokens in positive_tweet_tokens:
    positive_cleaned_tokens_list.append(remove_noise(tokens, stop_words))   # cleaning the dataset

for tokens in negative_tweet_tokens:
    negative_cleaned_tokens_list.append(remove_noise(tokens, stop_words))


def get_all_words(cleaned_tokens_list):         # used for seeing most common words
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


all_pos_words = get_all_words(positive_cleaned_tokens_list)
all_neg_words = get_all_words(negative_cleaned_tokens_list)
freq_dist_pos = FreqDist(all_pos_words)
freq_dist_neg = FreqDist(all_neg_words)
print(freq_dist_pos.most_common(20))        # most common positive words in dataset
print(freq_dist_neg.most_common(20))        # most common negative words in dataset


def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

positive_dataset = [(tweet_dict, "Positive")                            # creating the dictionary
                     for tweet_dict in positive_tokens_for_model]

negative_dataset = [(tweet_dict, "Negative")
                     for tweet_dict in negative_tokens_for_model]

dataset = positive_dataset + negative_dataset                   # total dataset, includes positives and negatives
random.shuffle(dataset)                             # shuffling it

train_data = dataset[:7000]         # train data consists of %70 of dataset
test_data = dataset[7000:]          # test data consists of %30 of dataset
classifier = NaiveBayesClassifier.train(train_data)         # classifying with Naive Bayes

print("Accuracy is:", classify.accuracy(classifier, test_data))     # accuracy of testing
print(classifier.show_most_informative_features(20))            # most informative 20 words of dataset

custom_tokens = remove_noise(word_tokenize(data))           # using our data
print(classifier.classify(dict([token, True] for token in custom_tokens)))
print(custom_tokens)

unique_words = set(custom_tokens)
freq_list = []

for words in unique_words:
    freq_list.append([custom_tokens.count(words), words])

i = 1
while i < 101:          # most common 100 words that accoun used
    print(sorted(freq_list)[-i])
    i += 1
