# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mindepth(self,root):
        if root.left==None and root.right==None:
            return 0
        elif root.left==None:
            leftheight = float('inf')
            rightheight = self.mindepth(root.right)
        elif root.right==None:
            rightheight = float('inf')
            leftheight  = self.mindepth(root.left)
        else:
            leftheight  = self.mindepth(root.left)
            rightheight = self.mindepth(root.right)
        return 1+min(leftheight,rightheight)
    def minDepth(self, root):
        if not root:
            return 0
        return 1+self.mindepth(root)
        