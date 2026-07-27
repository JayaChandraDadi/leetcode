# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def roottoleaf(self,root,s):
        if not root:
            return 
        s = s*10 + root.val
        if root.left==None and root.right==None:
            self.sum1+=s
            return 
        self.roottoleaf(root.left,s)
        self.roottoleaf(root.right,s)
 
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sum1 = 0
        self.roottoleaf(root,0)
        return self.sum1