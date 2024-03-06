python3 ./1-self-participle.py ./199801.txt ./word_list.txt ./CDIAL-BIAS-race.txt ./self.txt
python3 ./2-jieba-participle.py ./CDIAL-BIAS-race.txt ./result.txt
python3 ./3-calulator.py ./self.txt ./jieba.txt ./result.txt
# python3 ./3-calulator.py ./self-test.txt ./jieba-test.txt ./result.txt
