# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None :
            return 0
        
        if root.left == None and root.right == None :
            return 1
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/636058/Easy-to-understand-Python-Solutions-Iterative-(DFS)-and-Recursive
