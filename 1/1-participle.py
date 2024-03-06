import jieba
import sys

def segment_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    seg_list = jieba.cut(text, cut_all=False)
    segmented_text = " ".join(seg_list)

    with open(output_file_path, 'w', encoding='utf-8)') as file:
        file.write(f" {segmented_text}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 participle.py input_file_path output_file_path")
    else:
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        segment_file(input_file_path, output_file_path)

