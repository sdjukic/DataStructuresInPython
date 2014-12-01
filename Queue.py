# File that implements Queue ADT (FIFO).
# Supported operations:
#   enqueue(item) - put item in the queue
#   dequeue()     - takes element off the queue
#   is_empty()    - checks whether queue is empty
#
# Slavisa Djukic
# Nov. 28, 2014.

from Nodes import Node

class Queue(object):

  def __init__(self):
    self._size = 0
    self._head = Node("Dummy")
    self._tail = Node("Dummy")

  def dequeue(self):
    if self._size == 0:
      raise IndexError("Cannot dequeue empty queue.")
    result = self._head.next._node_data
    self._head.next = self._head.next.next
    self._size -= 1
    return result

  def enqueue(self, node_data):
    node = Node(node_data)
    if self._size == 0:
      self._head.next = node
      self._tail.next = node
    else:
      self._tail.next.next = node
      self._tail.next = node
    
    self._size += 1

  def is_empty(self):
    return self._size == 0
