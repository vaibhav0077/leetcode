# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or p == root  or q == root:
            return root
        
        lefty = self.lowestCommonAncestor(root.left, p , q)
        righty = self.lowestCommonAncestor(root.right, p , q)
        
        
        if not lefty: return righty
        elif not righty: return lefty
        else: return root
    
        