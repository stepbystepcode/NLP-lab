import jieba

def count_words_jieba(line, sensitive_words):
    word_counts = {word: 0 for word in sensitive_words}
    segmented_line = jieba.cut(line, cut_all=False)
    for word in segmented_line:
        if word in word_counts:
            word_counts[word] += 1
    return word_counts

def count_words_direct(line, sensitive_words):
    word_counts = {word: 0 for word in sensitive_words}
    for word in sensitive_words:
        word_counts[word] += line.count(word)
    return word_counts

def format_counts(counts_a, counts_b): # 3171
    return '\t'.join([f"{word}:{count_a}" for word, count_a in counts_a.items() if counts_a[word] != counts_b[word]])

def compare(input_file_path, sensitive_words_file_path, output_file_path):
    with open(sensitive_words_file_path, 'r', encoding='utf-8') as file:
        sensitive_words = [line.strip() for line in file.readlines()]

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            for line in input_file:
                line = line.strip().split('\t')[1]
                counts_jieba = count_words_jieba(line, sensitive_words)
                counts_direct = count_words_direct(line, sensitive_words)
                diff_counts_jieba = format_counts(counts_jieba, counts_direct)
                diff_counts_direct = format_counts(counts_direct, counts_jieba)
                if diff_counts_jieba or diff_counts_direct:
                    output_file.write(f"句子: {line}\n")
                    jieba_line = jieba.cut(line, cut_all=False)
                    cut_line = " ".join(jieba_line)
                    output_file.write(f"分词句子: {cut_line}\n")
                    output_file.write(f"分词统计: {diff_counts_jieba}\n")
                    output_file.write(f"直接统计: {diff_counts_direct}\n\n")

compare("./CDIAL-BIAS-race.txt", "./race.txt", "./output_res.txt")

