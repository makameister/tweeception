from elasticsearch import Elasticsearch
from lib.Dumper import Dumper
import json, requests, pprint
from tweepy import *
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk

"""""
Décommenter pour le premier lancement
"""""
# nltk.download('punkt')

"""
analyzer = SentimentIntensityAnalyzer()

sentence_en = "VADER is smart, handsome, and funny."
sentence_fr = "VADER est intelligent, beau et drôle FUCK !"
sentence_hard_fr = "VADER est intelligent, beau et drôle FUCK !"



sentence_hard_trans = "VADER est intelligent, beau et drôle FUCK !"

print(analyzer.polarity_scores("VADER est intelligent, beau et drôle."))
print(analyzer.polarity_scores(translation))

print("--------")

tokenized_sentence = nltk.word_tokenize(translation)

sid = SentimentIntensityAnalyzer()
pos_word_list = []
neu_word_list = []
neg_word_list = []

for word in tokenized_sentence:
    if (sid.polarity_scores(word)['compound']) >= 0.1:
        pos_word_list.append(word)
    elif (sid.polarity_scores(word)['compound']) <= -0.1:
        neg_word_list.append(word)
    else:
        neu_word_list.append(word)

print('Positive:', pos_word_list)
print('Neutral:', neu_word_list)
print('Negative:', neg_word_list)

elastic = Elasticsearch("15.236.56.178:9200")

# print("\nELASTICSEARCH INSTANCE:", elastic)
# print("CLIENT ATTRIBUTES:", dir(elastic))

# some_string = '{"hello" : "world"}'
# turn a JSON string into a dictionary:
# some_dict = json.loads(some_string)

search_param = {
    "query": {
        "terms": {
            "_id": [1234, 42]
        }
    }
}
# response = elastic.search(index="original", body=search_param)

response = elastic.search(index="original", body="")

# pprint.pprint(response, width=1)


"""