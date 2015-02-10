# Stack can be modeled by using list.
# Slavisa Djukic
# Nov. 28, 2014.

class Stack(object):

  def __init__(self):
    self._stack_container = []

  def push(self, item):
    """Push new item on the stack."""
    self._stack_container.append(item)


  def pop(self):
    """Pop element off the stack."""
    if len( self._stack_container ) == 0:
      raise IndexError("Cannot pop element from an empty stack!")
  
    return self._stack_container.pop()

  def top(self):
    """Look up the elemen on the top of the stack."""
    if len( self._stack_container ) == 0:
      raise IndexError("Stack is empty, cannot look up top element!")
    return self._stack_container[len(self._stack_container) - 1] 

  def is_empty(self):
    """Checks if the stack is empty."""
    return len(self._stack_container) == 0


