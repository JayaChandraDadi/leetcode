# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    sum1 = 0
    def leftsum(self,root,flag):
        if flag==1 and root.left==None and root.right==None:
            self.sum1+=root.val
            return 
        if root.left:
            self.leftsum(root.left,1)
        if root.right:
            self.leftsum(root.right,0)
    def sumOfLeftLeaves(self,root):
        self.leftsum(root,0)
        return self.sum1