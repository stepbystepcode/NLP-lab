import json

def load_hmm_parameters(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data['start_p'], data['trans_p'], data['emit_p']
def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    for y in states:
        V[0][y] = start_p[y] * emit_p[y].get(obs[0], 0)
        path[y] = [y]

    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((V[t-1][y0] * trans_p[y0].get(y, 0) * emit_p[y].get(obs[t], 0), y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        path = newpath

    n = len(obs) - 1
    (prob, state) = max((V[n][y], y) for y in states)
    return (prob, path[state])

with open('../data/199801_preprocessed.txt') as f:
    labeled_data = eval(f.read())
    num_elements = len(labeled_data) // 5
    labeled_data = labeled_data[-num_elements:]
    states = ['NA', 'SP', 'CP', 'SL', 'CL', 'SO', 'CO']
    words_array=[]
    result=""
    for data in labeled_data:
        words_array.append([element[0] for element in data])
    start_p, trans_p, emit_p = load_hmm_parameters('../data/hmm_parameters.json')
    for obs in words_array:
        for state in states:
            if state not in emit_p:
                emit_p[state] = {}
            for char in obs:
                if char not in emit_p[state]:
                    emit_p[state][char] = 0.01

        for state in states:
            if state not in trans_p:
                trans_p[state] = {}
            for next_state in states:
                if next_state not in trans_p[state]:
                    trans_p[state][next_state] = 0.01

        for state in states:
            if state not in start_p:
                start_p[state] = 0.01

        if len(obs) != 0:
            result += str(obs)+"\n"
            result += str(viterbi(obs, states, start_p, trans_p, emit_p))+"\n"
        with open('../data/saved.txt','w') as f:
            f.write(result)

