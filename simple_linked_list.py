#!/usr/bin/env python3

# Taken from Eric Schles python talk summer 2014

class Node(object):
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
    
    def __str__(self):
        return repr(self.item)


class LinkedList(object):
    """LinkedList class. Note that it is indexed from 1!"""
    def __init__(self):
        """Need 'dummy' root in python. Cannot handle insert at the beginging otherwise."""
        self.root = Node(1)
        self.size = 0

    def insert(self, position, node):
        if position > self.size + 1:
            raise AttributeError
        elif not self.root:
            self.root.next = node
        else:
            current = self.root
            counter = 1
            while counter < position:
                current = current.next
                counter += 1
            node.next = current.next
            current.next = node
        self.size += 1

    def selection_sort(self):
        if self.size > 1:
          counter = 1
          while counter < self.size:
              sorted_parent = self.root
              for _ in range(1, counter):
                sorted_parent = sorted_parent.next
              last_sorted = sorted_parent.next
              current_parent = last_sorted
              current = current_parent.next
              # if current is greater than the last sorted element 
              # it is in place, nothing to do
              if current.item < last_sorted.item:
                  temp = 0
                  temp_root_parent = self.root
                  while temp <= counter - 1:
                      temp_root = temp_root_parent.next
                      if temp_root.item > current.item:
                          temp_root_parent.next = current
                          current_parent.next = current.next
                          current.next = temp_root
                          break
                      temp_root_parent = temp_root_parent.next
                      temp += 1
                  temp += 1
              counter += 1
 
                      
              
              
              

    def traverse(self):
      counter = 1
      current = self.root.next
      while counter <= self.size:
          print(current)
          current = current.next
          counter += 1



if __name__ == '__main__':
    my_list = LinkedList()
    
  
    from random import randint

    # build the list here
    for i in range(1, 250):
        my_list.insert(1, Node(randint(1, 100000)))

    # now print it out
    my_list.traverse()

    # check sort
    my_list.selection_sort()
   
    print( "After sort" )
    my_list.traverse()
