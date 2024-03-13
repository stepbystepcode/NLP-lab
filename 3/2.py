import json
from sklearn.model_selection import train_test_split
import numpy as np
from collections import defaultdict

with open('../data/199801_preprocessed.txt', 'r', encoding='utf-8') as f:
    labeled_data = eval(f.read())
    index_to_slice = round(len(labeled_data) * (4/5))
    sliced_array = labeled_data[:index_to_slice]
train_data, test_data = train_test_split(sliced_array, test_size=0.2, random_state=42)

state_list = ['NA', 'SP', 'CP', 'SL', 'CL', 'SO', 'CO']
start_probability = defaultdict(int)
transition_probability = defaultdict(lambda: defaultdict(int))
emission_probability = defaultdict(lambda: defaultdict(int))
state_count = defaultdict(int)

for sentence in train_data:
    if not sentence: continue
    start_probability[sentence[0][1]] += 1
    previous_state = sentence[0][1]
    state_count[previous_state] += 1
    
    for word, state in sentence[1:]:
        transition_probability[previous_state][state] += 1
        emission_probability[state][word] += 1
        state_count[state] += 1
        previous_state = state
        
for word, state in sum(train_data, []):
    emission_probability[state][word] += 1

for state in start_probability:
    start_probability[state] /= len(train_data)

for prev_state in transition_probability:
    total_transitions = sum(transition_probability[prev_state].values())
    for state in transition_probability[prev_state]:
        transition_probability[prev_state][state] /= total_transitions

for state in emission_probability:
    total_emissions = sum(emission_probability[state].values())
    for word in emission_probability[state]:
        emission_probability[state][word] /= total_emissions

hmm_parameters = {
    "start_p": dict(start_probability),
    "trans_p": {state: dict(transition_probability[state]) for state in transition_probability},
    "emit_p": {state: dict(emission_probability[state]) for state in emission_probability}
}

with open('../data/hmm_parameters.json', 'w', encoding='utf-8') as f:
    json.dump(hmm_parameters, f, ensure_ascii=False, indent=2)
