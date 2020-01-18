'''
Convert Sorted Array to Binary Search Tree

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
=========================================
Simple tree traversal solution.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############
from typing import Dict, List
from tree_traversal import levelOrder
# from tree_helpers import TreeNode
class TreeNode:
    def __init__(self, val, left=None, right=None):
        '''Definition for binary tree.'''
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums: List[int]) -> TreeNode:
    if nums is None or len(nums) < 1: return None
    if len(nums) == 1: return TreeNode(nums[0])

    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid + 1:])

    return node

###########
# Testing #
###########

# Test 1
# Correct result =>
'''
      0
     / \
   -3   9
   /   /
 -10  5
'''
nums = [-10,-3,0,5,9]
node = sortedArrayToBST(nums)
print(levelOrder(node))

