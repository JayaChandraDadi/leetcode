# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def preorder(self,root,min1,max1):
        if not root:
            return True
        if min1>=root.val or root.val>=max1:
            return False
        return self.preorder(root.left,min1,root.val) and self.preorder(root.right,root.val,max1)  
    def isValidBST(self, root):
        return self.preorder(root,float('-inf'),float('inf'))