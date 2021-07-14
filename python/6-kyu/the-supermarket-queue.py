import numpy as np

def queue_time(customers, n):
    original_customers = customers.copy()

    if not(customers):
        return 0

    checkout = np.zeros(n)
    for i in range(n):
        if not(customers):
            return max(original_customers)
        checkout[i] = customers[0]
        customers.pop(0)

    if not(customers):
        return max(original_customers)

    counter = 0
    while True:
        if not(customers):
            break
        checkout -= 1
        counter += 1
        if 0 in checkout:
            index = (np.where(checkout == 0)[0])
            for i in range(index.size):
                checkout[index[i]] = customers[0]
                customers.pop(0)


    return int(counter + max(checkout))

print(queue_time([30, 9, 43, 26, 10, 5, 14, 12, 49, 33, 32, 26, 8], 3))
