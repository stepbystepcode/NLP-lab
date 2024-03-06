python3 1-participle.py ./CDIAL-BIAS-race.txt ./part.txt
python3 2-counting.py ./part.txt race.txt counting1.txt
python3 2-counting.py ./CDIAL-BIAS-race.txt ./race.txt ./counting2.txt
python3 3-compare.py ./counting1.txt ./counting2.txt
# grep -o '黑人' CDIAL-BIAS-race.txt | wc -l
