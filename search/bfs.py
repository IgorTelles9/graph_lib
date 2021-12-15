from structures.queue import Queue
import time
grafo = [[1,3,5], [0,2], [1,3,4,7], [0,2,4,5], [2,3,5,6,7], [0,3,4], [4,8], [2,4,8], [6,7]]

def bfs(s, arr):
    marker = [0 for x in range(len(arr))]
    queue = Queue() 
    queue_removed = []
    queue.push(s)
    marker[s] = 1

    while (len(queue) != 0):
        u = queue.pop()
        queue_removed.append(u)

        for item in arr[u]:
            if marker[item] == 0:
                marker[item] = 1
                queue.push(item)
    return (queue_removed)


start = time.time()
print(bfs(0,grafo))
finish = time.time()
print('time elapsed: ',finish-start)
