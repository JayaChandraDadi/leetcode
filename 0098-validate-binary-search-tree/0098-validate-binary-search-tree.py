# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def validate(self,root,min1,max1):
        if not root:
            return True
        if min1>=root.val or max1<=root.val:
            return False
        return self.validate(root.left,min1,root.val) and self.validate(root.right,root.val,max1)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root,float('-inf'),float('inf'))