def snail(snail_map):

    snail = []

    length = len(snail_map)
    for row_idx, row in enumerate(snail_map):
        for idx, n in enumerate(row):
            if row_idx == 0:
                snail.append(n)
            # if

            print(row, n, row_idx, idx)

    return snail


array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

expected = [1, 2, 3, 6, 9, 8, 7, 4, 5]

print(snail(array))
