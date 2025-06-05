# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def dfs(p,q):
            if  p!=None and q!=None and p.val==q.val:
                left = dfs(p.left,q.left)
                right = dfs(p.right,q.right)
            elif p==None and q==None:
                return True
            else:
                return False
            return left&right
        return dfs(p,q)
        