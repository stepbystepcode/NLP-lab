import sys
import ast
import re

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def extract_vocabulary(input_file_path):
    with open(input_file_path, 'r', encoding='gbk') as file:
        text = file.read()
    lines = text.strip().split('\n')
    vocabulary = set()
    for line in lines:
        words = line.split()
        for word in words:
            if '/' in word and word.split('/')[1] not in ['m', 'w']:
                word = word.split('/')[0]
                if word.startswith('['):
                    word = word[1:]
                vocabulary.add(word)
    return sorted(vocabulary)

def max_forward_matching(text, trie):
    max_word_length = 10
    start = 0
    segmented_text = []

    while start < len(text):
        matched = False
        for length in range(max_word_length, 0, -1):
            if start + length > len(text):
                continue
            substring = text[start:start + length]
            if trie.starts_with(substring):
                if trie.root.children.get(substring[-1], None) and trie.root.children[substring[-1]].is_end_of_word:
                    segmented_text.append(substring)
                    start += length
                    matched = True
                    break
        if not matched:
            segmented_text.append(text[start])
            start += 1

    return ' '.join(segmented_text)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 ./1-self-participle.py custom_segmentation_dict output_dict_path")
    else:
    input_vocab_file, output_vocab_file, input_text_file, output_text_file = sys.argv[1:5]

    vocabulary = extract_vocabulary(input_vocab_file)
    with open(output_vocab_file, 'w', encoding='utf-8') as file:
        file.write(str(vocabulary))

    trie = Trie()
    for word in vocabulary:
        trie.insert(word)

    with open(input_text_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    segmented_texts = ''
    for line in lines:
        clean_line = re.sub(r"^\d+\s+", "", line)
        segmented_text = max_forward_matching(clean_line, trie)
        segmented_texts += segmented_text
    with open(output_text_file, 'w', encoding='utf-8') as file:
        file.write(segmented_texts)
