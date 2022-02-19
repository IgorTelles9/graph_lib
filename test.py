import math
import random
from p_queue import PQueue
import time

def minKey(list):
 
        # Initialize min value
        min = math.inf
 
        for v in range(len(list)):
            if list[v] < min:
                min = list[v]
                min_index = v
 
        return min_index

start = time.time()
min = PQueue(100000)
finish = time.time()
print("tempo para heap ser criada com 100 000 espaços: " + str(finish-start) + "s")

start = time.time()
l = [math.inf] * 100000
finish = time.time()
print("tempo para lista criar 10 000 valores infinitos: " + str(finish-start) + "s")

# start = time.time()
# for i in range(10000):
#     n = random.randint(1,10)
#     l[i] = n
#     #min.update(i,n)
# finish = time.time()
# print("tempo para lista alocar 10 000 numeros aleatorios: " + str(finish-start) + "s")

# start = time.time()
# for i in range(10000):
#     l.pop(minKey(l))
# finish = time.time()

# print("tempo para lista achar o menor peso 10 000 vezes: " + str(finish-start) + "s")

start = time.time()
for i in range(100000):
    n = random.randint(1,10)
    min.update(i,n)

finish = time.time()
print("tempo para heap alocar (update) 100 000 numeros: " + str(finish-start) + "s")

start = time.time()
for i in range(100000):
    u = min.pop()
finish = time.time()

print("tempo para heap achar o minimo 100 000 vezes: " + str(finish-start) + "s")