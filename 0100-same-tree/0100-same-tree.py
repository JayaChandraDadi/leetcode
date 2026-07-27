# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def same(self,p,q):
        if p==None and q==None:
            return True
        if p==None and q!=None:
            return False
        if p!=None and q==None:
            return False
        if p.val!=q.val:
            return False
        return self.same(p.left,q.left) and self.same(p.right,q.right)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.same(p,q)