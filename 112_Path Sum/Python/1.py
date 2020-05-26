# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None :
            return False
        if root.left == None and root.right == None :
            return root.val == sum
        if root.left == None :
            return self.hasPathSum(root.right, sum - root.val)
        if root.right == None :
            return self.hasPathSum(root.left, sum - root.val)
        return self.hasPathSum(root.right, sum - root.val) or self.hasPathSum(root.left, sum - root.val)
        
        https://leetcode.com/problems/path-sum/discuss/651443/Python-99
