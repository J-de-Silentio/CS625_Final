from queue import Queue
from queue import PriorityQueue

###############################

que = Queue()

que.put(0); temp = que.get()

print(f"Popped element: '{temp}'")

###############################

pq = PriorityQueue()

pq.put(0);temp = pq.get()

print(f"Popped element: '{temp}'")
