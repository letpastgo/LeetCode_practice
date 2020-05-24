# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        def helper(node, level) :
            if node == None :
                return None
            if len(res) == level :
                res.append([])
            res[level].append(node.val)
            helper(node.left, level + 1)
            helper(node.right, level + 1)
            
        
        helper(root, 0)
        res.reverse()
        
        return res
        
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/639454/Python-3-DFS

