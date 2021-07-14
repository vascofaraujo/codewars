def recoverSecret(triplets):
    #print(triplets)

    string = []
    print(string)
    for t in triplets:
        print("t: " + str(t))
        for i, c in enumerate(t):
            print("c, i: " + c + str(i))
            #print(t[i])
            if i == 0 :
                print("0\n")
                print(string, t)

                if t[i+1] in string:
                    if t[i] in string:
                        #if string.index(t[i+1]) > string.index(t[i]):
                        #    continue
                        print("here")
                        old_index = string.index(t[i])
                        string.pop(old_index)
                    new_index = string.index(t[i+1])
                    string.insert(new_index,c)

                else:
                    if t[i] not in string:
                        string.append(c)
            if i == 1:
                print("1\n")
                print(string, t)

                if t[i-1] in string:
                    if t[i] in string:
                        if string.index(t[i-1]) < string.index(t[i]):
                            continue
                        print("here")
                        old_index = string.index(t[i])
                        string.pop(old_index)
                    new_index = string.index(t[i-1])+1
                    string.insert(new_index,c)
                elif t[i+1] in string:
                    if t[i] in string:
                        #if string.index(t[i+1]) > string.index(t[i]):
                        #    continue
                        print("here")
                        old_index = string.index(t[i])
                        string.pop(old_index)
                    new_index = string.index(t[i+1])
                    string.insert(new_index,c)

                else:
                    if t[i] not in string:
                        string.append(c)
            if i == 2:
                print("2\n")
                print(string, t)

                if t[i-1] in string:
                    if t[i] in string:
                        if string.index(t[i-1]) < string.index(t[i]):
                            continue
                        print("here")
                        old_index = string.index(t[i])
                        string.pop(old_index)
                    new_index = string.index(t[i-1])+1
                    string.insert(new_index,c)

                else:
                    if t[i] not in string:
                        string.append(c)
    print(string)
    return -1

secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]

print(recoverSecret(triplets))
