# Node class that is base for all recursive datastructures

class Node(object):
    def __init__(self, data=None, next=None):
      self._node_data = data
      self.next = next

    def __str__(self):
      return repr(self._node_data)

class BinaryNode(object):
    def __init__(self, data=None, right_child=None, left_child=None):
      self._node_data = data
      self._right_child = right_child
      self._left_child = left_child

    def __str__(self):
      return repr(self._node_data)


