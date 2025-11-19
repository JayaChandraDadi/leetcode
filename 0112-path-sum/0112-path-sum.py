# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathsum(self,root,target):
        if not root:
            return False
        if root.left==None and root.right==None:
            return target==root.val
        leftsum = self.pathsum(root.left,target-root.val)
        rightsum = self.pathsum(root.right,target-root.val)
        return leftsum or rightsum
    def hasPathSum(self, root, targetSum):
        if not root:
            return False
        return self.pathsum(root,targetSum)