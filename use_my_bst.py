#!/usr/bin/env python

from BinarySearchTree import BinarySearchTree

my_tree = BinarySearchTree()
n = [25, 50, 12, 5, 35]
for i in n:
  my_tree.insert(i)

c = my_tree._root
c = c.next
while c != None:
  print(c)
  c = c._left_child
