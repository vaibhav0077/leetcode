# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #function to calculate sum upto a node using depth first approach
    def currentsum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            left = max(0,self.currentsum(root.left))
            right = max(0,self.currentsum(root.right))
            #comparing for max
            self.max=max(self.max,root.val+left+right)
            #returning one side of node only as both sides can't form a single path to grandparent
            return root.val+max(right, left)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max=root.val
        self.currentsum(root)
        return self.max
