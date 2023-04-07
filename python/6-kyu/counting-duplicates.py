def duplicate_count(text):
    # Your code goes here
    dup = 0
    dup_list = []
    for i,c in enumerate(text):
        for c2 in range(i+1,len(text)):
            if text[c2].upper() == c.upper() and not(text[c2] in dup_list):
                dup=dup+1
                dup_list.append(c.lower())
                dup_list.append(c.upper())
                continue
    return dup
