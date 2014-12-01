#!/usr/env/bin python3

# File that uses BST
from BST import BST

bst = BST(25)
bst.insert(12)
bst.insert(50)
bst.insert(6)
bst.insert(45)
bst.insert(1)

print("Does tree contain 1 {0}".format(bst.contains(1)))
print("Does tree contain 5 {0}".format(bst.contains(5)))
print("Does tree contain 12 {0}".format(bst.contains(12)))
print("Does tree contain 51 {0}".format(bst.contains(51)))



