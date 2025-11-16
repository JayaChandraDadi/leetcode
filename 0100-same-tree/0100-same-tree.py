# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def check(self,temp1,temp2):
        if temp1==None and temp2==None:
            return True
        if temp1==None or temp2==None:
            return False
        if temp1.val!=temp2.val:
            return False
        return self.check(temp1.left,temp2.left) and self.check(temp1.right,temp2.right)
    def isSameTree(self, p, q):
        return self.check(p,q)

        