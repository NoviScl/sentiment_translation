#to get all sentences with special words from larger dataset
with open("special_words", "r") as f:
	special_words = f.readline().strip().split(',')

indices = [[] for i in range(len(special_words))]
en_sents = [[] for i in range(len(special_words))]

for w in range(len(special_words)):
	indices[w] = []

f_z = open("/Users/sichenglei/Desktop/sentiment-analysis/datasets/ai_challenger_translation_train_20170912/translation_train_20170912/train.zh", 'r')
f_e = open("/Users/sichenglei/Desktop/sentiment-analysis/datasets/ai_challenger_translation_train_20170912/translation_train_20170912/train.en", 'r')

f_zh = list(f_z)
f_en = list(f_e)

for i in range(len(f_en)):
	for w in special_words:
		if w in f_en[i].strip().split():
			indices[special_words.index(w)].append(i)

f_en_w = open('datasets/sents_w_special.en', 'w')
f_zh_w = open('datasets/sents_w_special.zh', 'w')

for w in range(len(special_words)):
	for sent in indices[w]:
		f_en_w.write(f_en[sent])
		f_zh_w.write(f_zh[sent])

f_z.close()
f_e.close()
f_zh_w.close()
f_en_w.close()


# counts: 
# slick 241
# rampant 306
# unrestrained 57
# stubborn 576
# entice 186
# proud 5593
# awesome 1098
# shrewd 142
# naive 395
