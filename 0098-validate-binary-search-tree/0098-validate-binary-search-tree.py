# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def validate(self,node,min1,max1):
        if node==None:
            return True
        if node.val<=min1 or node.val>=max1:
            return False
        return self.validate(node.left,min1,node.val) and self.validate(node.right,node.val,max1)
    def isValidBST(self, root):
        return self.validate(root,float('-inf'),float('inf'))