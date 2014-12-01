# Pure python implementation of Binary Search Tree 

from Nodes import BinaryNode
from Nodes import Node

class BinarySearchTree(object):
  def __init__(self):
    self._root = Node("dummy")
  
  def find(self, value):
    current_node = self._root.next
    
    while current_node and current_node._node_data != value:
      if current_node._node_data >  value:
        current_node = current_node._left_child
      elif current_node._node_data < value:
        current_node = current_node._right_child

    return current_node != None

  def insert(self, value):
    if not self._root.next:
      self._root.next = BinaryNode(value)
    else:
      current_node = self._root.next
      while True:
        if current_node._node_data >  value:
          if current_node._left_child == None:
            current_node._left_child = BinaryNode(value)
            break;
          else:
            current_node = current_node._left_child

        elif current_node._node_data < value:
          if current_node._right_child == None:
            current_node._right_child = BinaryNode(value)
            break;
          else:
            current_node = current_node._right_child
        else:
          raise AttributeError("Value aready present.")
    
  def _inorder_successor(self, node):
    """Method returns value of the inorder successor of the given node."""
    pass

  def delete(self, value):
    if not self._root.next:
      raise AttributeError("Cannot delete from an empty tree.")
    else:
      pass
  


