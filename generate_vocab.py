#generate vocab form datasets
import codecs 
import collections
from operator import itemgetter 

#raw data are all in the datasets folder
DATA_DIR = "datasets/TED/"
datasets = ["train.txt.en", "train.txt.zh"]

RAW_DATA = DATA_DIR + datasets[0]
VOCAB_OUTPUT = "en.vocab"

with open("special_words", "r") as f:
	special_words = f.readline().strip().split(',')

print (special_words)

def generate_vocab(RAW_DATA, VOCAB_OUTPUT, VOCAB_SIZE):
	counter = collections.Counter()
	with codecs.open(RAW_DATA, 'r', 'utf-8') as f:
		for line in f:
			for word in line.strip().split():
				counter[word] += 1

	#sort by word frequency
	sorted_word_to_cnt = sorted(
		counter.items(), key=itemgetter(1), reverse=True)

	sorted_words = [x[0] for x in sorted_word_to_cnt]

	sorted_words = ["<unk>", "<sos>", "<eos>"] 



