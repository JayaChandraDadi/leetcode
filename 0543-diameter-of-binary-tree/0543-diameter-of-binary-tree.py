# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    maxi = 0
    def diameter(self,root):
        if root==None:
            return 0
        leftheight = self.diameter(root.left)
        rightheight = self.diameter(root.right)
        self.maxi = max(self.maxi,leftheight+rightheight)
        return 1+max(leftheight,rightheight)
    def diameterOfBinaryTree(self, root):
        self.diameter(root)
        return self.maxi