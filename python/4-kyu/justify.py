def justify(text, width):
    word = text.split()

    num_chars = 0
    justify = []
    line = []
    for i in word:
        num_chars += sum(len(w) for w in i)
        # print(len(line) + 1 + num_chars, len(line) +1,num_chars, i)
        if num_chars < width:
            line.append(i)
            line.append(' ')
            num_chars += 1
        else:
            print("hello", line)
            line.pop()

            line.append('\n')
            # line.append(i)
            justify += line
            line = []
            line.append(i)
            num_chars = 0

        print(justify, line)
    print(justify)
    return ''.join(justify)

if __name__ == '__main__':
    print(justify('123 45 6', 7))#, '123  45\n6'))
