#tokenize english data
perl ./tokenizer.perl -no-escape -l "en" < ../datasets/TED/train.raw.en > ../datasets/TED/train_b.txt.en 
perl ./tokenizer.perl -no-escape -l "en" < ../datasets/newsComm/raw_newsComm.en > ../datasets/newsComm/newsComm.en 

#tokenizer chinese data
sed 's/ //g; s/./& /g' ../datasets/TED/train.raw.zh > ../datasets/TED/train.txt.zh
sed 's/ //g; s/./& /g' ../datasets/newsComm/raw_newsComm.zh > ../datasets/newsComm/newsComm.zh
