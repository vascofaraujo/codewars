import time
import numpy as np
start_time = time.time()

def josephus_survivor(n,k):

    circle = np.arange(1,n+1)
    counter = 0
    t = 0

    while(len(circle) > 1):
        #print(circle)
        circle_to_remove = np.zeros(len(circle))
        t = 0
        for i in circle:
            counter += 1
            if counter == k:
                circle_to_remove[t] = int(np.where(circle==int(i))[0])
                t += 1
                counter = 0
        circle_to_remove = circle_to_remove[0:t]
        for j in np.flipud(circle_to_remove):
            circle = np.delete(circle,int(j))

    if (np.any(circle)):
        return int(circle[0])
    else:
        return n

print(josephus_survivor(14, 2))

# print(josephus_survivor(4607,2798))#4265
# print( josephus_survivor(4777,1971))
# print( josephus_survivor(4777,1971))
# print( josephus_survivor(4777,1971))
# print( josephus_survivor(4777,1971))
# print( josephus_survivor(4777,1971))
# print( josephus_survivor(4777,1971))
# print( josephus_survivor(4777,1971))

print("--- %s seconds ---" % (time.time() - start_time))
