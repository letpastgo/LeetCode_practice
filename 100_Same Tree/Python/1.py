# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p == None or q == None :
            return p == q
        if p.val != q.val :
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            
https://leetcode.com/problems/same-tree/discuss/618246/Python-simple-and-elegant-solution
