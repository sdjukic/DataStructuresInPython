from Queue import Queue
from Queue import Node

my_queue = Queue()

for i in xrange(10000):
  my_queue.enqueue(i*2)

while not my_queue.is_empty():
  print(my_queue.dequeue())

