import sys
def count_sensitive_words(segmented_file_path, sensitive_words_file_path, output_file_path):
    with open(sensitive_words_file_path, 'r', encoding='utf-8') as file:
        sensitive_words = [line.strip() for line in file.readlines()]
    
    word_counts = {word: 0 for word in sensitive_words}
    
    with open(segmented_file_path, 'r', encoding='utf-8') as file:
        for line in file:
            for word in sensitive_words:
                word_counts[word] += line.count(word)
    
    print(word_counts.items())
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1])
    
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for word, count in sorted_word_counts:
            file.write(f"#{word}: {count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 2-counting.py input_file_path sensitive_words_file_path output_file_path")
    else:
        segmented_file_path = sys.argv[1]
        sensitive_words_file_path = sys.argv[2]
        output_file_path = sys.argv[3]
        count_sensitive_words(segmented_file_path, sensitive_words_file_path, output_file_path)
        print('Done.');

