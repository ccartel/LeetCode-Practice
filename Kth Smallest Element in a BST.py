230. Kth Smallest Element in a BST
Medium
10.2K
181
Companies
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

 

Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    temp = 0

    def dfs(node, curr):
        nonlocal k, temp
        if node is not None:
            dfs(node.left, curr)
            k -= 1
            if k == 0:
                temp = node.val
                return
            dfs(node.right, curr)
    dfs(root, k)
    return temp
