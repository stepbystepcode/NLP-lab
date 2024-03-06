import sys
from collections import Counter

def evaluate_segmentation(file1, file2, output_file):
    precision_all=0
    recall_all=0
    F1_all=0
    num=0
    with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    with open(output_file, 'w', encoding='utf-8') as out:
        for line1, line2 in zip(lines1, lines2):
            words1 = Counter(line1.strip().split())
            words2 = Counter(line2.strip().split())

            common = words1 & words2
            TP = sum(common.values())
            FP = sum((words2 - words1).values())
            FN = sum((words1 - words2).values())

            precision = TP / (TP + FP) if (TP + FP) else 0
            recall = TP / (TP + FN) if (TP + FN) else 0
            F1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) else 0
            precision_all = precision_all + precision
            recall_all = recall_all + recall
            F1_all = F1_all + F1
            num=num+1

            out.write("自定义分词:\t" + line1)
            out.write("jieba分词:\t" + line2)
            out.write(f"准确率:{precision:.3f}\n")
            out.write(f"召回率:{recall:.3f}\n")
            out.write(f"F测度:{F1:.3f}\n")
            out.write("---\n")
        print(f"总准确率:{precision_all/num:.3f}")
        print(f"总召回率:{recall_all/num:.3f}")
        print(f"总F测度:{F1_all/num:.3f}")

if len(sys.argv) != 4:
    print("Usage: python3 ./3-calulator.py file1_path file2_path output_path")
else:
    file1_path = sys.argv[1]
    file2_path = sys.argv[2]
    output_path = sys.argv[3]
    evaluate_segmentation(file1_path, file2_path, output_path)
