def to_weird_case(string):
    #TODO
    new_string = []
    split = string.split()
    for s in split:
        for index,c in enumerate(s):
            print(index, c)
            if int(index) % 2 == 0:
                new_string.append(c.upper())
            else:
                new_string.append(c.lower())
        new_string.append(" ")
    new_string.pop()
    return "".join(new_string)

print(to_weird_case('Weird string case'))
