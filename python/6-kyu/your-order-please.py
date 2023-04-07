import numpy as np
def order(sentence):
    # code here
    split = sentence.split()
    final_sentence = np.zeros(len(split), dtype=object)

    for word in split:
        for i in range(1,10):
            if str(i) in word:
                final_sentence[i-1] = word

    final_sentence = " ".join(final_sentence)
    return final_sentence
