from lib.DataFetcher import DataFetcher
from lib.DataProcessor import DataProcessor
import pprint
import nltk

"""""
Décommenter pour le premier lancement
"""""
nltk.download('punkt')


d = DataFetcher()

print(d.fetchFromElastic())
# install pprint
# pprint.pprint(d.fetchFromElastic())

sentence_1 = "VADER is smart, handsome, and funny."
sentence_2 = "VADER est intelligent, beau et drôle FUCK !"
sentence_3 = "VADER est intelligent, beau et drôle FUCK !"
sentences = [sentence_1, sentence_2, sentence_3]

p = DataProcessor()
p.process(sentences)

print('-------------------------')
print('Polarités :')
print('-------------------------')
pprint.pprint(p.getPolarities())
print('-------------------------')
print('Phrases et listes de mots par type :')
print('-------------------------')
pprint.pprint(p.getSentences())
print('-------------------------')
print('Words count :')
print('-------------------------')
pprint.pprint(p.getWordsCount())

