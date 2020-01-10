
"""
Tree Traversal
Pre-order: Root, Left, Right
In-order: Left, Root, Right
Post-order: Left, Right, Root
Level-order(Breadth first):

URL: https://charlesliuyx.github.io/2018/10/22/%E3%80%90%E7%9B%B4%E8%A7%82%E7%AE%97%E6%B3%95%E3%80%91%E6%A0%91%E7%9A%84%E5%9F%BA%E6%9C%AC%E6%93%8D%E4%BD%9C/
(【直观算法】二叉树遍历算法总结)
URL: https://gist.github.com/thinkphp/1439668
=========================================
Solution

    Time Complexity:    O(N)
    Space Complexity:   O(N)
"""

############
# Solution #
############

from collections import deque
from typing import Dict, List

# from tree_helpers import TreeNode
class TreeNode:
    def __init__(self, val, left=None, right=None, level=None):
        '''Definition for binary tree.'''
        self.val = val
        self.left = left
        self.right = right
        self.level = level

# Root, Left, Right
def preorderTraversalRecursively(root: TreeNode) -> List[int]:
    result = []
    if root:
        result += [root.val]
        result += preorderTraversalRecursively(root.left)
        result += preorderTraversalRecursively(root.right)
    return result

def preorderTraversal(root: TreeNode) -> List[int]:
    if not root: return []
    
    result, stack = [], [root] # Initialize a stack, FILO
    while stack:
        cur_node = stack.pop() # Access root
        result.append(cur_node.val)

        if cur_node.right: # Put right node into stack at first
            stack.append(cur_node.right)

        if cur_node.left: # Then put left node, so when pop stack left will be visited at first
            stack.append(cur_node.left)
            
    return result

# Left, Root, Right
def inorderTraversalRecursively(root: TreeNode) -> List[int]:
    result = []
    if root:
        result += inorderTraversalRecursively(root.left)
        result += [root.val]
        result += inorderTraversalRecursively(root.right)
    return result

def inorderTraversal(root: TreeNode) -> List[int]:
    if not root: return []

    result, stack = [], [] # Initialize a stack, FILO
    while root or stack:
        if root:
            stack.append(root)

            root = root.left
        else:
            root = stack.pop()
            result.append(root.val)

            root = root.right

    return result

# Left, Right, Root
def postorderTraversalRecursively(root: TreeNode) -> List[int]:
    result = []
    if root:
        result += postorderTraversalRecursively(root.left)
        result += postorderTraversalRecursively(root.right)
        result += [root.val]
    return result

# Almost the same as preorderTraversal(), just two stack.append() execute in different order and result is reversed
def postorderTraversal(root: TreeNode) -> List[int]:
    if root is None: return []

    result, stack = [], [root] # Initialize a stack, FILO
    while stack:
        cur_node = stack.pop()
        result.append(cur_node.val)

        if cur_node.left:
            stack.append(cur_node.left)

        if cur_node.right:
            stack.append(cur_node.right)

    return result[::-1]

# Breadth first
def levelOrder(root: TreeNode) -> List[List[int]]:
    if root is None: return []

    root.level, current_level = 1, 1
    result, queue = [], deque([root]) # Initialize a queue, FIFO
    level_nodes = []  # Record the nodes for each level

    while len(queue) > 0:
        cur_node = queue.popleft()

        if (cur_node.level > current_level):
            current_level += 1

            result.append(level_nodes)
            level_nodes = []

        level_nodes.append(cur_node.val)

        if cur_node.left:
            cur_node.left.level = current_level + 1
            queue.append(cur_node.left)

        if cur_node.right:
            cur_node.right.level = current_level + 1
            queue.append(cur_node.right)

    result.append(level_nodes) # Don't forget the last leaves
    return result

###########
# Testing #
###########

# Test 1
# Correct result =>
'''
 5
/ \
1  4
  / \
 3   6
'''
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))

print(preorderTraversalRecursively(root))
print(preorderTraversal(root))
print(inorderTraversalRecursively(root))
print(inorderTraversal(root))
print(postorderTraversalRecursively(root))
print(postorderTraversal(root))
print(levelOrder(root))

# Test 2
# Correct result =>
'''
  1
 / \
 2  3
/ \  \
4  5  6
  / \
  7  8
'''
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))), TreeNode(3, None, TreeNode(6)))

print(preorderTraversalRecursively(root))
print(preorderTraversal(root))
print(inorderTraversalRecursively(root))
print(inorderTraversal(root))
print(postorderTraversalRecursively(root))
print(postorderTraversal(root))
print(levelOrder(root))