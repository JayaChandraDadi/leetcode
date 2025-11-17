# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getheight(self,root):
        if root==None:
            return 0
        leftheight = self.getheight(root.left)
        rightheight = self.getheight(root.right)
        return 1+max(leftheight,rightheight)
    def isBalanced(self, root):
        if not root:
            return True
        leftheight = self.getheight(root.left)
        rightheight = self.getheight(root.right)
        if abs(leftheight-rightheight)<=1  and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
