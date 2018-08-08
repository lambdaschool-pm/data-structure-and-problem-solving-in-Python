# Data Structures, Algorithms and Problem Solving in Python

## Topics:
  * [ ] Lists
  * [ ] Linked Lists
  * [ ] Queues
  * [ ] Stacks
  * [ ] Sets
  * [ ] Maps
  * [ ] Hash Tables
  * [ ] Binary Search Trees
  * [ ] Trie
  * [ ] Heaps
  * [ ] Graphs
  * [ ] Breath First Search - BFS
  * [ ] Depth First Search - DFS
  * [ ] Adjacent Lists
  * [ ] Adjacent Matrix
  * [ ] Incident Matrix

## Tasks
### Data Structures
[ ] Linked Lists

### Problems

#### Problem 1
* [ ] Done

  Given a list of numbers and a number k, return whether any two numbers from the list add up to k. 
  
  For example, given ```[10, 15, 3, 7]``` and k of 17, return true since ```10 + 7 is 17``.


#### Problem 2
* [ ] Done

  Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

  For example, if our input was ```[1, 2, 3, 4, 5]```, the expected output would be ```[120, 60, 40, 30, 24]```. If our input was ```[3, 2, 1]```, the expected output would be ```[2, 3, 6]```.

  Follow-up: what if you can't use division?

#### Problem 3
* [ ] Done

  Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

  For example, given the following Node class
  ```
  class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  The following test should pass:

  node = Node('root', Node('left', Node('left.left')), Node('right'))
  assert deserialize(serialize(node)).left.left.val == 'left.left'
  ```