import jieba
import sys
import re

def segment_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(output_file_path, 'w', encoding='utf-8') as file:
        for line in lines:
            line = re.sub(r"^\d+\s+", "", line)
            seg_list = jieba.cut(line, cut_all=False)
            segmented_text = " ".join(seg_list)
            file.write(f"{segmented_text}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 ./2-jieba-participle.py input_file_path output_file_path")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        segment_file(input_file_path, output_file_path)


