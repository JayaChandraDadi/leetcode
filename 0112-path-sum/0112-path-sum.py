# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def path(self,root,targetsum):
        if not root:
            return False
        if root.left==None and root.right==None:
            return targetsum==root.val
        return self.path(root.left,targetsum-root.val) or self.path(root.right,targetsum-root.val)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.path(root,targetSum)