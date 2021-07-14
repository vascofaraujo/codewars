def recoverSecret(triplets):

    string = []
    for t in triplets:
        print(t)
        print(string)
        print("\n")
        in_string = []

        for i in range(3):
            if t[i] in string:
                in_string.append(i)
        print(in_string)

        for j in in_string:
            if j != 2:
                if not(string.index(t[j] < string.index[t[j+1]])):
                    string.pop(string.index(t[j]))
                    string.insert(string.index(t[j+1]), t[j])

        for i in range(3):
            if not(t[i] in string):
                string.append(t[i])


        """
        if not(t[2] in string):
            string.append(t[2])

        if t[1] in string:
            if not(string.index(t[1]) < string.index(t[2])):
                string.pop(string.index(t[1]))
                string.insert(string.index(t[2]), t[1])
        else:
            string.insert(string.index(t[2]), t[1])

        if t[0] in string:
            if not(string.index(t[0]) < string.index(t[1])):
                string.pop(string.index(t[0]))
                string.insert(string.index(t[1]), t[0])
        else:
            string.insert(string.index(t[1]), t[0])
        """

    return "".join(string)

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
