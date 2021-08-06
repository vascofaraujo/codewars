import numpy as np

def count_lives_and_deaths(cell, x, y):
    live_neigbors = 0
    dead_neighbors = 0
    #print(cell, x, y)
    # print(cell.shape)
    if x == 0:
        start_x = 0
    else:
        start_x = x-1
    if x == cell.shape[1]-1:
        end_x = cell.shape[1]-1
    else: end_x = x+1
    if y == 0:
        start_y = 0
    else:
        start_y = y-1
    if y == cell.shape[0]-1:
        end_y = cell.shape[0]-1
    else: end_y = y+1

    for a in range(start_x, end_x+1):
        for b in range(start_y, end_y+1):
            if cell[a,b] == 1:
                live_neigbors += 1
            else: dead_neighbors += 1


    if cell[x,y] == 1:
        live_neigbors -= 1
    else: dead_neighbors -= 1

    return live_neigbors, dead_neighbors

def remove_empty(cell):
    mask = (cell == 0)
    rows = np.flatnonzero((~mask).sum(axis=1))
    cols = np.flatnonzero((~mask).sum(axis=0))

    cell = cell[rows.min():rows.max()+1, cols.min():cols.max()+1]
    return cell

def get_generation(cells, generations):
    cell = np.asarray(cells)
    n = generations*2
    m = int(n/2)

    new_cell = np.zeros((cell.shape[0]+n, cell.shape[1]+n), dtype="int")
    cols, rows = new_cell.shape
    for x in range(m,cols-m):
        for y in range(m,rows-m):
            new_cell[x,y] = cell[x-m,y-m]

    cell = new_cell
    cell_new_gen = cell.copy()
    while generations > 0:
        for x in range(cols-1):
            for y in range(rows-1):
                live_neigbors, dead_neighbors = count_lives_and_deaths(cell, x, y)

                if cell[x,y] == 1:
                    if live_neigbors < 2:
                        cell_new_gen[x,y] = 0
                    elif live_neigbors > 3:
                        cell_new_gen[x,y] = 0
                    else:
                        pass
                else:
                    if live_neigbors == 3:
                        cell_new_gen[x,y] = 1

        cell = cell_new_gen
        cell_new_gen = cell.copy()

        generations -= 1

    cell = remove_empty(cell)

    return cell.tolist()



start = [[1, 1, 1, 0, 0, 0, 1, 0],
         [1, 0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 1, 1, 1]]


print(get_generation(start, 16))
