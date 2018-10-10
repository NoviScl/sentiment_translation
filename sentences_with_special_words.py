#generate vocab form datasets
import codecs 
import collections
from operator import itemgetter 

#raw data are all in the datasets folder
DATA_DIR = "datasets/TED/"
datasets = ["train.txt.en", "train.txt.zh"]

RAW_DATA = DATA_DIR + datasets[0]

with open("special_words", "r") as f:
	special_words = f.readline().strip().split(',')

print (special_words)

counter = collections.Counter()
with codecs.open(RAW_DATA, 'r', 'utf-8') as f:
	for line in f:
		for word in line.strip().split():
			counter[word] += 1

for w in special_words:
	print (w, counter[w])

# slick 26
# rampant 26
# unrestrained 40
# stubborn 51
# entice 9
# proud 222
# awesome 107
# shrewd 39
# naive 86

