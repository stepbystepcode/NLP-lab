def preprocess_and_label(text):
    sentences = text.strip().split('\n')
    labeled_data = []

    for sentence in sentences:
        words = sentence.split()[1:]
        labeled_sentence = []
        
        for word in words:
            char, tag = word.split('/')

            
            if tag == 'nr':
                nr_count += 1
                if nr_count % 2 == 1:
                    if len(char) > 1:
                        labeled_sentence.append((char[0], 'SP'))
                        for c in char[1:]:
                            labeled_sentence.append((c, 'CP'))
                    else:
                        labeled_sentence.append((char, 'SP'))
                else:
                    for c in char:
                        labeled_sentence.append((c, 'CP'))

            
            elif tag == 'ns':
                if len(char) > 1:
                    labeled_sentence.append((char[0], 'SL'))
                    for c in char[1:]:
                        labeled_sentence.append((c, 'CL'))
                else:
                    labeled_sentence.append((char, 'SL'))
            elif tag == 'nt':
                if len(char) > 1:
                    labeled_sentence.append((char[0], 'SO'))
                    for c in char[1:]:
                        labeled_sentence.append((c, 'CO'))
                else:
                    labeled_sentence.append((char, 'SO'))
            else:
                for c in char:
                    labeled_sentence.append((c, 'NA'))
        labeled_data.append(labeled_sentence)

    return labeled_data

with open('../data/199801.txt', 'r', encoding='gbk') as f:
    text = f.read()
    labeled_data = preprocess_and_label(text)
    with open('../data/199801_preprocessed.txt', 'w', encoding='utf-8') as f:
        f.write(str(labeled_data))
