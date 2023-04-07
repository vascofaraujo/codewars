def anagrams(word, words):
    unique_characters = {}
    for i in word:
        if i in unique_characters:
            unique_characters[i] = unique_characters.get(i)+1
        else:
            unique_characters[i] = 1

    anagrams = []
    for w in words:
        b = unique_characters.copy()
        for i in w:
            if i in b:
                b[i] = b.get(i)-1
            else:
                break
        if all(value==0 for value in b.values()):
            anagrams.append(w)

    return anagrams

print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
