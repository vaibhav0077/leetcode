# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValidBST(root, minV, maxV):
            
            if not root: return True
            
            if root.val >= maxV or root.val <= minV: return False
            
            return isValidBST(root.left, minV, root.val) and isValidBST(root.right, root.val, maxV)
    
        return isValidBST(root, float('-inf'), float('inf'))
            
            
            
        