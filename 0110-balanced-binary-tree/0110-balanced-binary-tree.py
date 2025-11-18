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
        if leftheight==-1:
            return -1
        rightheight = self.getheight(root.right)
        if rightheight==-1:
            return -1
        if abs(leftheight-rightheight)>1:
            return -1
        return 1+max(leftheight,rightheight)
    def isBalanced(self, root):
        if self.getheight(root)==-1:
            return False
        else:
            return True
        