# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,root):
        if root==None:
            return 0
        leftheight = self.check(root.left)
        rightheight = self.check(root.right)
        return 1+ max(leftheight,rightheight)
    def maxDepth(self, root):
        return self.check(root)