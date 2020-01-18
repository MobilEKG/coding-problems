'''
Symmetric Tree

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
=========================================
Simple tree traversal solution.
    Time Complexity:    O(N)
    Space Complexity:   O(N)
'''


############
# Solution #
############

# from tree_helpers import TreeNode
class TreeNode:
    def __init__(self, val, left=None, right=None):
        '''Definition for binary tree.'''
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: TreeNode) -> bool:
    queue = [root, root]

    while queue:
        t1 = queue.pop(0)
        t2 = queue.pop(0)

        if (t1 == None and t2 == None):
            continue
        if (t1 == None or t2 == None):
            return False

        if t1.val != t2.val:
            return False
        else:
            queue.append(t1.left)
            queue.append(t2.right)
            queue.append(t1.right)
            queue.append(t2.left)

    return True

###########
# Testing #
###########

# Test 1
# Correct result => True
'''
    1
   / \
  2   2
 / \ / \
3  4 4  3
'''
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(isSymmetric(root))

# Test 2
# Correct result => False
'''
    1
   / \
  2   2
   \   \
   3    3
'''
root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(isSymmetric(root))