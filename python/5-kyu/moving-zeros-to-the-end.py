def move_zeros(array):
    num_zeros = 0
    length = len(array)
    i = 0

    while i < length:
        number = array[i]
        if number == 0:
            array.pop(i)
            num_zeros = num_zeros + 1
            i -= 1
            length -= 1
        i += 1


    for i in range(num_zeros):
        array.append(0)
    return array
