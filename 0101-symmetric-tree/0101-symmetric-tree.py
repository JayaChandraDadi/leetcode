# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,left,right):
        if left==None and right==None:
            return True
        if left==None or right==None:
            return False
        if left.val!=right.val:
            return False
        return self.check(left.left,right.right) and self.check(left.right,right.left)
        return True
    def isSymmetric(self, root):
        return self.check(root.left,root.right)
