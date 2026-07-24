# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanced(self,root):
        if root==None:
            return 0
        leftheight = self.balanced(root.left)
        if leftheight==-1:
            return -1
        rightheight = self.balanced(root.right)
        if rightheight==-1:
            return -1
        if abs(leftheight-rightheight)>1:
            return -1
        return 1+max(leftheight,rightheight)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.balanced(root)!=-1
        