# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lca(self,root,p,q):
        if root==None or root==p or root==q:
            return root
        left = self.lca(root.left,p,q)
        right = self.lca(root.right,p,q)
        if left==None:
            return right
        if right==None:
            return left
        return root
    def lowestCommonAncestor(self, root, p, q):
       return self.lca(root,p,q)
        